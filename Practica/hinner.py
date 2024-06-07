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


@dataclass
class TreeNode:
    name: str
    children: list
    type: str = None

class TreeVisitor(hinnerVisitor):
    def __init__(self):
        self.definiciones = []
        self.lastType = ''

    def visitRoot(self, ctx: hinnerParser.RootContext):
        print(f'Root: {ctx.getText()}')
        children = [self.visit(child) for child in ctx.getChildren()]
        return TreeNode(name='root', children=children)
    
    def visitDefDef(self, ctx: hinnerParser.DefDefContext):
        [expr, _, seña] = list(ctx.getChildren())
        print(f'DefDef: {expr.getText()} :: {seña.getText()}')
        seña = self.visit(seña)
        self.definiciones.append((expr.getText(), seña.type))
        return TreeNode(name='::', children=[self.visit(expr), seña])
    
    def visitUniseñaDef(self, ctx: hinnerParser.UniseñaDefContext):
        [variable] = list(ctx.getChildren())
        print(f'UniseñaDef: {variable.getText()}')
        return TreeNode(name=variable.getText(), children=[], type=variable.getText())
    
    def visitMultiseñaDef(self, ctx: hinnerParser.MultiseñaDefContext):
        [variable, _, seña] = list(ctx.getChildren())
        print(f'MultiseñaDef: {variable.getText()} -> {seña.getText()}')
        seña = self.visit(seña)
        return TreeNode(name=variable.getText(), children=[seña], type=f'({variable.getText()} -> {seña.type})')

    def visitNumberExpr(self, ctx: hinnerParser.NumberExprContext):
        [number] = list(ctx.getChildren())
        print(f'NumberExpr: {number.getText()}')
        type = None
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == number.getText():
                    type = definicion[1]
                    break
        if type == None:
            type = nextType(self.lastType)
            self.lastType = type
            self.definiciones.append((number.getText(), type))
        return TreeNode(name=number.getText(), children=[], type=type)

    def visitVariableExpr(self, ctx: hinnerParser.VariableExprContext):
        return self.visit(ctx.getChild(0))

    def visitPlusExpr(self, ctx: hinnerParser.PlusExprContext):
        print(f'PlusExpr: {ctx.getText()}')
        type = None
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == '(+)':
                    type = definicion[1]
                    break
        if type == None:
            type = nextType(self.lastType)
            self.lastType = type
            self.definiciones.append(('(+)', type))
        return TreeNode(name='(+)', children=[], type=type)

    def visitLambdaExpr(self, ctx: hinnerParser.LambdaExprContext):
        print(f'LambdaExpr: {ctx.getText()}')
        return self.visit(ctx.getChild(0))

    def visitLambdaDef(self, ctx: hinnerParser.LambdaDefContext):
        [_, variable, _, expr] = list(ctx.getChildren())
        type = None
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == ctx.getText():
                    type = definicion[1]
                    break
        if type == None:
            type = nextType(self.lastType)
            self.lastType = type
            self.definiciones.append((ctx.getText(), type))
        print(f'LambdaDef: {variable.getText()} -> {expr.getText()}, type: {type}')
        return TreeNode(name='λ', children=[self.visit(variable), self.visit(expr)], type=type)

    def visitApplicationDef(self, ctx: hinnerParser.ApplicationDefContext):
        [expr1, expr2] = list(ctx.getChildren())
        print(f'ApplicationDef: {expr1.getText()} {expr2.getText()}')
        type = None
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == ctx.getText():
                    type = definicion[1]
                    break
            if type == None:
                type = nextType(self.lastType)
                self.lastType = type
                self.definiciones.append((ctx.getText(), type))
        return TreeNode(name='@', children=[self.visit(expr1), self.visit(expr2)], type=type)
    
    def visitParenthesis(self, ctx: hinnerParser.ParenthesisContext):
        [_, expr, _] = list(ctx.getChildren())
        print(f'Parenthesis: {expr.getText()}')
        return self.visit(expr)
    
    def visitExprDef(self, ctx: hinnerParser.ExprDefContext):
        return self.visit(ctx.getChild(0))
    
    def visitVariableDef(self, ctx: hinnerParser.VariableDefContext):
        [variable] = list(ctx.getChildren())
        print(f'VariableDef: {variable.getText()}')
        type = None
        if self.definiciones:
            for definicion in self.definiciones:
                if definicion[0] == variable.getText():
                    type = definicion[1]
                    break
        if type == None:
            type = nextType(self.lastType)
            self.lastType = type
            self.definiciones.append((variable.getText(), type))
        return TreeNode(name=variable.getText(), children=[], type=type)

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = hinnerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hinnerParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    if parser.getNumberOfSyntaxErrors() == 0:
        return visitor.visit(tree), visitor.definiciones
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
            tree, definiciones = tree
            if definiciones:
                st.write('Definiciones:')
                st.table(definiciones)
            for child in tree.children:
                if isinstance(child, TreeNode) and child.name != '::':
                    dot = render_tree(child)
                    st.graphviz_chart(dot)
            print("Tree:")
            print(tree)
        else:
            st.write(f"Syntax errors: {tree[0]}\n{tree[1]}")
    else:
        st.write("Please enter some text to parse.")
