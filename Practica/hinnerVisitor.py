# Generated from hinner.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hinnerParser import hinnerParser
else:
    from hinnerParser import hinnerParser

# This class defines a complete generic visitor for a parse tree produced by hinnerParser.

class hinnerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hinnerParser#root.
    def visitRoot(self, ctx:hinnerParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#defDef.
    def visitDefDef(self, ctx:hinnerParser.DefDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#uniseñaDef.
    def visitUniseñaDef(self, ctx:hinnerParser.UniseñaDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#multiseñaDef.
    def visitMultiseñaDef(self, ctx:hinnerParser.MultiseñaDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#numberExpr.
    def visitNumberExpr(self, ctx:hinnerParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#variableExpr.
    def visitVariableExpr(self, ctx:hinnerParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#plusExpr.
    def visitPlusExpr(self, ctx:hinnerParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:hinnerParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#lambdaDef.
    def visitLambdaDef(self, ctx:hinnerParser.LambdaDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#applicationDef.
    def visitApplicationDef(self, ctx:hinnerParser.ApplicationDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#exprDef.
    def visitExprDef(self, ctx:hinnerParser.ExprDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#parenthesis.
    def visitParenthesis(self, ctx:hinnerParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#variableDef.
    def visitVariableDef(self, ctx:hinnerParser.VariableDefContext):
        return self.visitChildren(ctx)



del hinnerParser