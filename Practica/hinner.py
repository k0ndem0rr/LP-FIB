import streamlit as st
from antlr4 import *
from hinnerLexer import hinnerLexer
from hinnerParser import hinnerParser
from hinnerVisitor import hinnerVisitor
from dataclasses import dataclass
from graphviz import Digraph

# grammar hinner;

# root : 
#     (('\t'|'\r'|application|lambda|def) '\n')+
#     ;
# def:
#     expr '::' seña #defDef
#     ;

# seña:
#     VARIABLE #uniseñaDef
#     | VARIABLE '->' seña #multiseñaDef
#     ;

# expr :
#     NUMBER                  # numberExpr
#     | VARIABLE              # variableExpr
#     | '(+)'                 # plusExpr
#     | lambda                # lambdaExpr 
#     ;

# lambda : 
#     '\\' VARIABLE '->' application #lambdaDef
#     ;
# application : 
#     application expr      #applicationDef
#     | '(' application ')'  #parenthesis
#     | expr                 #exprDef
#     ;


# NUMBER     : [0-9]+ ;
# VARIABLE   : [a-zA-Z]+ ;
# WS         : [ \t\r\n]+ -> skip ;




@dataclass
class TreeNode:
    name: str
    children: list

class TreeVisitor(hinnerVisitor):
    def __init__(self):
        self.definiciones = []

    def visitRoot(self, ctx: hinnerParser.RootContext):
        print(f'Root: {ctx.getText()}')
        children = [self.visit(child) for child in ctx.getChildren()]
        return TreeNode(name='root', children=children)
    
    def visitDefDef(self, ctx: hinnerParser.DefDefContext):
        [expr, _, seña] = list(ctx.getChildren())
        print(f'DefDef: {expr.getText()} :: {seña.getText()}')
        self.definiciones.append((expr.getText(), seña.getText()))
        return TreeNode(name='::', children=[self.visit(expr), self.visit(seña)])
    
    def visitUniseñaDef(self, ctx: hinnerParser.UniseñaDefContext):
        [variable] = list(ctx.getChildren())
        print(f'UniseñaDef: {variable.getText()}')
        return TreeNode(name=variable.getText(), children=[])
    
    def visitMultiseñaDef(self, ctx: hinnerParser.MultiseñaDefContext):
        [variable, _, seña] = list(ctx.getChildren())
        print(f'MultiseñaDef: {variable.getText()} -> {seña.getText()}')
        return TreeNode(name=variable.getText(), children=[self.visit(seña)])

    def visitNumberExpr(self, ctx: hinnerParser.NumberExprContext):
        [number] = list(ctx.getChildren())
        print(f'NumberExpr: {number.getText()}')
        return TreeNode(name=number.getText(), children=[])

    def visitVariableExpr(self, ctx: hinnerParser.VariableExprContext):
        [variable] = list(ctx.getChildren())
        print(f'VariableExpr: {variable.getText()}')
        return TreeNode(name= variable.getText(), children=[])

    def visitPlusExpr(self, ctx: hinnerParser.PlusExprContext):
        print(f'PlusExpr: {ctx.getText()}')
        return TreeNode(name='(+)', children=[])

    def visitLambdaExpr(self, ctx: hinnerParser.LambdaExprContext):
        print(f'LambdaExpr: {ctx.getText()}')
        return self.visit(ctx.getChild(0))

    def visitLambdaDef(self, ctx: hinnerParser.LambdaDefContext):
        [_, variable, _, expr] = list(ctx.getChildren())
        print(f'LambdaDef: {variable.getText()} -> {expr.getText()}')
        return TreeNode(name='λ', children=[variable.getText(), self.visit(expr)])

    def visitApplicationDef(self, ctx: hinnerParser.ApplicationDefContext):
        [expr1, expr2] = list(ctx.getChildren())
        print(f'ApplicationDef: {expr1.getText()} {expr2.getText()}')
        return TreeNode(name='@', children=[self.visit(expr1), self.visit(expr2)])
    
    def visitParenthesis(self, ctx: hinnerParser.ParenthesisContext):
        [_, expr, _] = list(ctx.getChildren())
        print(f'Parenthesis: {expr.getText()}')
        return self.visit(expr)
    
    def visitExprDef(self, ctx: hinnerParser.ExprDefContext):
        return self.visit(ctx.getChild(0))

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
        dot.node(name='root', label=node.name)
        parent = 'root'
    for child in node.children:
        if isinstance(child, TreeNode):
            child_id = str(id(child))
            dot.node(name=child_id, label=child.name)
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
            for child in tree.children:
                if isinstance(child, TreeNode):
                    dot = render_tree(child)
                    st.graphviz_chart(dot)
            if definiciones:
                st.write('Definiciones:')
                st.table(definiciones)
        else:
            st.write(f"Syntax errors: {tree[0]}\n{tree[1]}")
    else:
        st.write("Please enter some text to parse.")
