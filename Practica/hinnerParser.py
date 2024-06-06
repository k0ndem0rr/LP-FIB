# Generated from hinner.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,32,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,32,0,9,1,0,0,0,2,19,1,0,0,
        0,4,21,1,0,0,0,6,26,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,
        0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,20,5,6,0,0,14,20,5,
        7,0,0,15,16,5,1,0,0,16,20,5,6,0,0,17,20,3,4,2,0,18,20,3,6,3,0,19,
        13,1,0,0,0,19,14,1,0,0,0,19,15,1,0,0,0,19,17,1,0,0,0,19,18,1,0,0,
        0,20,3,1,0,0,0,21,22,5,2,0,0,22,23,5,7,0,0,23,24,5,3,0,0,24,25,3,
        2,1,0,25,5,1,0,0,0,26,27,5,4,0,0,27,28,3,4,2,0,28,29,3,2,1,0,29,
        30,5,5,0,0,30,7,1,0,0,0,2,11,19
    ]

class hinnerParser ( Parser ):

    grammarFileName = "hinner.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'(+)'", "'\\'", "'->'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "VARIABLE", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_lambda = 2
    RULE_application = 3

    ruleNames =  [ "root", "expr", "lambda", "application" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    VARIABLE=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hinnerParser.ExprContext)
            else:
                return self.getTypedRuleContext(hinnerParser.ExprContext,i)


        def getRuleIndex(self):
            return hinnerParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hinnerParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.expr()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 214) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(hinnerParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(hinnerParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class LambdaExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambda_(self):
            return self.getTypedRuleContext(hinnerParser.LambdaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpr" ):
                return visitor.visitLambdaExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(hinnerParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ApplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def application(self):
            return self.getTypedRuleContext(hinnerParser.ApplicationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplicationExpr" ):
                return visitor.visitApplicationExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = hinnerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = hinnerParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(hinnerParser.NUMBER)
                pass
            elif token in [7]:
                localctx = hinnerParser.VariableExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(hinnerParser.VARIABLE)
                pass
            elif token in [1]:
                localctx = hinnerParser.AddExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(hinnerParser.T__0)
                self.state = 16
                self.match(hinnerParser.NUMBER)
                pass
            elif token in [2]:
                localctx = hinnerParser.LambdaExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.lambda_()
                pass
            elif token in [4]:
                localctx = hinnerParser.ApplicationExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 18
                self.application()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_lambda

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LambdaDefContext(LambdaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.LambdaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(hinnerParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaDef" ):
                return visitor.visitLambdaDef(self)
            else:
                return visitor.visitChildren(self)



    def lambda_(self):

        localctx = hinnerParser.LambdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lambda)
        try:
            localctx = hinnerParser.LambdaDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(hinnerParser.T__1)
            self.state = 22
            self.match(hinnerParser.VARIABLE)
            self.state = 23
            self.match(hinnerParser.T__2)
            self.state = 24
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_application

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ApplicationDefContext(ApplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ApplicationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambda_(self):
            return self.getTypedRuleContext(hinnerParser.LambdaContext,0)

        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplicationDef" ):
                return visitor.visitApplicationDef(self)
            else:
                return visitor.visitChildren(self)



    def application(self):

        localctx = hinnerParser.ApplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_application)
        try:
            localctx = hinnerParser.ApplicationDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(hinnerParser.T__3)
            self.state = 27
            self.lambda_()
            self.state = 28
            self.expr()
            self.state = 29
            self.match(hinnerParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





