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


    # Visit a parse tree produced by hinnerParser#numberExpr.
    def visitNumberExpr(self, ctx:hinnerParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#variableExpr.
    def visitVariableExpr(self, ctx:hinnerParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#addExpr.
    def visitAddExpr(self, ctx:hinnerParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:hinnerParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#applicationExpr.
    def visitApplicationExpr(self, ctx:hinnerParser.ApplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#lambdaDef.
    def visitLambdaDef(self, ctx:hinnerParser.LambdaDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hinnerParser#applicationDef.
    def visitApplicationDef(self, ctx:hinnerParser.ApplicationDefContext):
        return self.visitChildren(ctx)



del hinnerParser