import streamlit as st
from antlr4 import *
from hinnerLexer import hinnerLexer
from hinnerParser import hinnerParser
from hinnerVisitor import hinnerVisitor
# grammar hinner;

# root : 
#     expr+
#     ;

# expr :
#     NUMBER                  # numberExpr
#     | VARIABLE              # variableExpr
#     | '(' '+' NUMBER ')'    # addExpr
#     | lambda                # lambdaExpr 
#     | application           # applicationExpr
#     ;

# lambda : 
#     '\\' VARIABLE '-> expr' #lambdaDef
#     ;
# application : 
#     '(' lambda expr ')'     #applicationDef
#     ;


# NUMBER     : [0-9]+ ;
# VARIABLE   : [a-zA-Z]+ ;
# WS         : [ \t\r\n]+ -> skip ;



class TreeVisitor(hinnerVisitor):
    def __init__(self):
        self.nivell = 0
    def visitNumberExpr(self, ctx: hinnerParser.NumberExprContext):
        [number] = list(ctx.getChildren())
        print('  ' * self.nivell + 'number ' + number.getText())
    def visitVariableExpr(self, ctx: hinnerParser.VariableExprContext):
        [variable] = list(ctx.getChildren())
        print('  ' * self.nivell + 'variable ' + variable.getText())
    def visitAddExpr(self, ctx: hinnerParser.AddExprContext):
        [_, number] = list(ctx.getChildren())
        print('  ' * self.nivell + 'add ' + number.getText())
    def visitLambdaExpr(self, ctx: hinnerParser.LambdaExprContext):
        [lambda_expr] = list(ctx.getChildren())
        self.visit(lambda_expr)
    def visitApplicationExpr(self, ctx: hinnerParser.ApplicationExprContext):
        [app_expr] = list(ctx.getChildren())
        self.visit(app_expr)
    def visitLambdaDef(self, ctx: hinnerParser.LambdaDefContext):
        [_, variable, _, expr] = list(ctx.getChildren())
        print('  ' * self.nivell + 'lambda ' + variable.getText())
        self.nivell += 1
        self.visit(expr)
        self.nivell -= 1
    def visitApplicationDef(self, ctx: hinnerParser.ApplicationDefContext):
        [_, lambda_expr, expr, _] = list(ctx.getChildren())
        print('  ' * self.nivell + 'application')
        self.nivell += 1
        self.visit(lambda_expr)
        self.visit(expr)
        self.nivell -= 1
    
    
    

# input_stream = FileStream('input.hinner')
# lexer = hinnerLexer(input_stream)
# token_stream = CommonTokenStream(lexer)
# parser = hinnerParser(token_stream)
# tree = parser.root()


# if parser.getNumberOfSyntaxErrors() == 0:
#     visitor = TreeVisitor()
#     visitor.visit(tree)
# else:
#     print(parser.getNumberOfSyntaxErrors(), "errors found")
#     print(tree.toStringTree(recog=parser))

st.title('Hinner')
input_text = st.text_area('Input')
if st.button('Run'):
    with open('input.hinner', 'w') as f:
        f.write(input_text)
    input_stream = FileStream('input.hinner')
    lexer = hinnerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hinnerParser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = TreeVisitor()
        visitor.visit(tree)
    else:
        print(parser.getNumberOfSyntaxErrors(), "errors found")
        print(tree.toStringTree(recog=parser))