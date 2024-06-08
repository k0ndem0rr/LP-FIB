import streamlit as st
from antlr4 import *
from hinnerLexer import hinnerLexer
from hinnerParser import hinnerParser
from hinnerVisitor import hinnerVisitor
from dataclasses import dataclass
from graphviz import Digraph

# grammar hinner;

# root : 
#     (('\t'|'\r'|application|lambda|def) '\n'*)* 
#     (('\t'|'\r'|application|lambda|def))? 
#     ;
# def:
#     application '::' seña   #defDef
#     ;

# seña:
#     variable                #uniseñaDef
#     | variable '->' seña    #multiseñaDef
#     ;

# expr :
#     NUMBER                  # numberExpr
#     | variable              # variableExpr
#     | '(+)'                 # plusExpr
#     | lambda                # lambdaExpr 
#     ;

# lambda : 
#     '\\' variable '->' application #lambdaDef
#     ;
# application : 
#     application expr        #applicationDef
#     | '(' application ')'   #parenthesis
#     | expr                  #exprDef
#     ;

# variable : 
#     VARIABLE                #variableDef
#     ;

# NUMBER     : [0-9]+ ;
# VARIABLE   : [a-zA-Z]+ ;
# WS         : [ \t\r\n]+ -> skip ;





def nextType(type: str):
    if type == "":
        return "a"

    # Convertir la cadena en una lista de caracteres para facilitar la manipulación
    type_list = list(type)
    
    # Empezar desde el final de la cadena
    for i in range(len(type_list) - 1, -1, -1):
        if type_list[i] == 'z':
            # Si el carácter actual es 'z', se convierte en 'a'
            type_list[i] = 'a'
        else:
            # Incrementar el carácter actual y terminar
            type_list[i] = chr(ord(type_list[i]) + 1)
            break
    else:
        # Si hemos convertido todas las 'z' en 'a', agregar una 'a' al principio
        type_list.insert(0, 'a')
    
    # Unir la lista de caracteres en una cadena y devolverla
    return ''.join(type_list)

#(N->(N->N)) : (N->N)
def simplifyLastParenthesis(type: str):
    if type == "" or type == None or type[0] != '(':
        return ("",type)

    # Convertir la cadena en una lista de caracteres para facilitar la manipulación
    type_list = list(type)
    entryType = ""
    # Empezar desde el principio de la cadena
    for i in range(len(type_list)):
        if type_list[0] == '-':
            break
        if type_list[0] != '(':
            entryType += type_list[0]
        type_list.pop(0)
    type_list.pop(0)
    type_list.pop(0)

    # Empezar desde el final de la cadena
    type_list.pop(-1)

    # Unir la lista de caracteres en una cadena y devolverla
    print(f"entryType: {entryType}, type_list: {''.join(type_list)}")
    return (entryType, ''.join(type_list))
        
def defineType(self, var):
    type = None
    if self.definiciones:
        for definicion in self.definiciones:
            if definicion[0] == var.getText():
                type = definicion[1]
                if self.entryType != "" and type != self.entryType:
                    self.errorMsg = f"Error: {var.getText()} no es de tipo {self.entryType}, es de tipo {type}"
                    print(f"Error: {var.getText()} no es de tipo {self.entryType}, es de tipo {type}")
                    self.appType = ""
                break
    if type == None:
        if self.appType != '':
            type = self.appType
            self.definiciones.append((var.getText(), type))
        else:
            type = nextType(self.lastRandomType)
            self.lastRandomType = type
    return type

@dataclass
class TreeNode:
    name: str
    children: list
    type: str = None

class TreeVisitor(hinnerVisitor):
    def __init__(self):
        self.definiciones = []
        self.lastRandomType = ''
        self.appType = ''
        self.entryType = ''
        self.errorMsg = ''

    def visitRoot(self, ctx: hinnerParser.RootContext):
        print(f"/n")
        children = [self.visit(child) for child in ctx.getChildren()]
        
        return TreeNode(name='root', children=children)
    
    def visitInvalidDef(self, ctx: hinnerParser.InvalidDefContext):
        return None
    
    def visitDefDef(self, ctx: hinnerParser.DefDefContext):
        [expr, _, seña] = list(ctx.getChildren())
        seña = self.visit(seña)
        self.definiciones.append((expr.getText(), seña.type))
        return TreeNode(name='::', children=[self.visit(expr), seña])
    
    def visitUniseñaDef(self, ctx: hinnerParser.UniseñaDefContext):
        [variable] = list(ctx.getChildren())
        return TreeNode(name=variable.getText(), children=[], type=variable.getText())
    
    def visitMultiseñaDef(self, ctx: hinnerParser.MultiseñaDefContext):
        [variable, _, seña] = list(ctx.getChildren())
        seña = self.visit(seña)
        return TreeNode(name=variable.getText(), children=[seña], type=f'({variable.getText()}->{seña.type})')

    def visitNumberExpr(self, ctx: hinnerParser.NumberExprContext):
        [number] = list(ctx.getChildren())
        return TreeNode(name=number.getText(), children=[], type=defineType(self, number))

    def visitVariableExpr(self, ctx: hinnerParser.VariableExprContext):
        return self.visit(ctx.getChild(0))

    def visitPlusExpr(self, ctx: hinnerParser.PlusExprContext):
        type = defineType(self, ctx.getChild(0))
        return TreeNode(name='(+)', children=[], type=type)

    def visitLambdaExpr(self, ctx: hinnerParser.LambdaExprContext):
        return self.visit(ctx.getChild(0))

    def visitLambdaDef(self, ctx: hinnerParser.LambdaDefContext):
        [_, variable, _, expr] = list(ctx.getChildren())
        type = None
        expr = self.visit(expr)
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == ctx.getText():
                    type = definicion[1]
                    break
        if type == None:
            if self.appType != '':
                type = f'({self.entryType}->{self.appType})'
                self.appType = type
                self.definiciones.append((ctx.getText(), type))
            else:
                type = nextType(self.lastRandomType)
                self.lastRandomType = type
        return TreeNode(name='λ', children=[self.visit(variable), expr], type=type)

    def visitApplicationDef(self, ctx: hinnerParser.ApplicationDefContext):
        [expr1, expr2] = list(ctx.getChildren())

        #Le doy un tipo provisional a la aplicación
        type = nextType(self.lastRandomType)
        self.lastRandomType = type

        #Visito el primer hijo de la aplicación
        expr1 = self.visit(expr1)

        #Extraigo el tipo de la aplicación y el tipo de la entrada
        type0, type1 = simplifyLastParenthesis(expr1.type)
        self.entryType = type0
        self.appType = type1

        #Si el tipo de la entrada es vacío, entonces la aplicación no tiene tipo
        if self.entryType == "":
            self.appType = ""
        expr2 = self.visit(expr2)
        if self.appType == "":
            self.entryType = ''
        else:
            type = self.appType
        self.definiciones.append((f'{ctx.getText()}', type))
        return TreeNode(name='@', children=[expr1, expr2], type=type)
    
    def visitParenthesis(self, ctx: hinnerParser.ParenthesisContext):
        [_, expr, _] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitExprDef(self, ctx: hinnerParser.ExprDefContext):
        return self.visit(ctx.getChild(0))
    
    def visitVariableDef(self, ctx: hinnerParser.VariableDefContext):
        [variable] = list(ctx.getChildren())
        print(f'VariableDef: {variable.getText()}, entryType: {self.entryType}, appType: {self.appType}')
        type = None
        
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == variable.getText():
                    type = definicion[1]
                    if type != self.entryType:
                        self.errorMsg = f"Error: {variable.getText()} no es de tipo {self.entryType}"
                        print(f"Error: {variable.getText()} no es de tipo {self.entryType}")
                        self.appType = ""
                    break
        if type == None:
            if self.appType != '':
                type = self.appType
                self.definiciones.append((variable.getText(), type))
            else:
                type = nextType(self.lastRandomType)
                self.lastRandomType = type
        return TreeNode(name=variable.getText(), children=[], type=type)
    
    def visitVariableParenthesis(self, ctx: hinnerParser.VariableParenthesisContext):
        return self.visit(ctx.getChild(0))

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = hinnerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hinnerParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    if parser.getNumberOfSyntaxErrors() == 0:
        return visitor.visit(tree), visitor.definiciones, visitor.errorMsg
    else:
        return parser.getNumberOfSyntaxErrors(), tree.toStringTree(recog=parser)

def render_tree(node, dot=None, parent=None):
    if dot is None:
        dot = Digraph()
        dot.node(name='root', label=node.name + (f" \n {node.type}" if node.type else ''))
        parent = 'root'
    for child in node.children:
        if isinstance(child, TreeNode) and child.name != '::':
            child_id = str(id(child))
            dot.node(name=child_id, label=child.name  + (f" \n {child.type}" if child.type else ''))
            dot.edge(parent, child_id)
            child.appType = ""
            child.entryType = ""
            render_tree(child, dot, child_id)
        else:
            child_id = str(id(child))
            dot.node(name=child_id, label=str(child))
            dot.edge(parent, child_id)
        
    return dot

st.title('Hinner')

input_text = st.text_area('Input')
if st.button('Run'):
    if input_text:
        tree = parse_input(input_text)
        if isinstance(tree, tuple) and isinstance(tree[0], TreeNode):
            tree, definiciones, errorMsg = tree
            if definiciones:
                st.write('Definiciones:')
                st.table(definiciones)
            if errorMsg:
                st.write(errorMsg)
            for child in tree.children:
                if isinstance(child, TreeNode) and child.name != '::':
                    dot = render_tree(child)
                    st.graphviz_chart(dot)
        else:
            st.write(f"Syntax errors: {tree[0]}\n{tree[1]}")
    else:
        st.write("Please enter some text to parse.")
