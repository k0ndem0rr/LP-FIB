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
        4,1,12,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,3,0,18,8,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,
        1,0,1,0,1,0,3,0,31,8,0,3,0,33,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,
        2,3,2,43,8,2,1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,62,8,5,1,5,1,5,5,5,66,8,5,10,5,12,5,69,9,
        5,1,5,0,1,10,6,0,2,4,6,8,10,0,0,80,0,22,1,0,0,0,2,34,1,0,0,0,4,42,
        1,0,0,0,6,48,1,0,0,0,8,50,1,0,0,0,10,61,1,0,0,0,12,18,5,1,0,0,13,
        18,5,2,0,0,14,18,3,10,5,0,15,18,3,8,4,0,16,18,3,2,1,0,17,12,1,0,
        0,0,17,13,1,0,0,0,17,14,1,0,0,0,17,15,1,0,0,0,17,16,1,0,0,0,18,19,
        1,0,0,0,19,21,5,3,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,
        22,23,1,0,0,0,23,32,1,0,0,0,24,22,1,0,0,0,25,31,5,1,0,0,26,31,5,
        2,0,0,27,31,3,10,5,0,28,31,3,8,4,0,29,31,3,2,1,0,30,25,1,0,0,0,30,
        26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,33,1,0,0,
        0,32,30,1,0,0,0,32,33,1,0,0,0,33,1,1,0,0,0,34,35,3,6,3,0,35,36,5,
        4,0,0,36,37,3,4,2,0,37,3,1,0,0,0,38,43,5,11,0,0,39,40,5,11,0,0,40,
        41,5,5,0,0,41,43,3,4,2,0,42,38,1,0,0,0,42,39,1,0,0,0,43,5,1,0,0,
        0,44,49,5,10,0,0,45,49,5,11,0,0,46,49,5,6,0,0,47,49,3,8,4,0,48,44,
        1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,7,1,0,0,0,50,
        51,5,7,0,0,51,52,5,11,0,0,52,53,5,5,0,0,53,54,3,10,5,0,54,9,1,0,
        0,0,55,56,6,5,-1,0,56,57,5,8,0,0,57,58,3,10,5,0,58,59,5,9,0,0,59,
        62,1,0,0,0,60,62,3,6,3,0,61,55,1,0,0,0,61,60,1,0,0,0,62,67,1,0,0,
        0,63,64,10,3,0,0,64,66,3,6,3,0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,11,1,0,0,0,69,67,1,0,0,0,8,17,22,30,32,
        42,48,61,67
    ]

class hinnerParser ( Parser ):

    grammarFileName = "hinner.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\t'", "'\\r'", "'\\n'", "'::'", "'->'", 
                     "'(+)'", "'\\'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "VARIABLE", "WS" ]

    RULE_root = 0
    RULE_def = 1
    RULE_seña = 2
    RULE_expr = 3
    RULE_lambda = 4
    RULE_application = 5

    ruleNames =  [ "root", "def", "seña", "expr", "lambda", "application" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMBER=10
    VARIABLE=11
    WS=12

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

        def application(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hinnerParser.ApplicationContext)
            else:
                return self.getTypedRuleContext(hinnerParser.ApplicationContext,i)


        def lambda_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hinnerParser.LambdaContext)
            else:
                return self.getTypedRuleContext(hinnerParser.LambdaContext,i)


        def def_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hinnerParser.DefContext)
            else:
                return self.getTypedRuleContext(hinnerParser.DefContext,i)


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
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 17
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 12
                        self.match(hinnerParser.T__0)
                        pass

                    elif la_ == 2:
                        self.state = 13
                        self.match(hinnerParser.T__1)
                        pass

                    elif la_ == 3:
                        self.state = 14
                        self.application(0)
                        pass

                    elif la_ == 4:
                        self.state = 15
                        self.lambda_()
                        pass

                    elif la_ == 5:
                        self.state = 16
                        self.def_()
                        pass


                    self.state = 19
                    self.match(hinnerParser.T__2) 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3526) != 0):
                self.state = 30
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 25
                    self.match(hinnerParser.T__0)
                    pass

                elif la_ == 2:
                    self.state = 26
                    self.match(hinnerParser.T__1)
                    pass

                elif la_ == 3:
                    self.state = 27
                    self.application(0)
                    pass

                elif la_ == 4:
                    self.state = 28
                    self.lambda_()
                    pass

                elif la_ == 5:
                    self.state = 29
                    self.def_()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_def

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefDefContext(DefContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.DefContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)

        def seña(self):
            return self.getTypedRuleContext(hinnerParser.SeñaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefDef" ):
                return visitor.visitDefDef(self)
            else:
                return visitor.visitChildren(self)



    def def_(self):

        localctx = hinnerParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_def)
        try:
            localctx = hinnerParser.DefDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.expr()
            self.state = 35
            self.match(hinnerParser.T__3)
            self.state = 36
            self.seña()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeñaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_seña

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiseñaDefContext(SeñaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.SeñaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(hinnerParser.VARIABLE, 0)
        def seña(self):
            return self.getTypedRuleContext(hinnerParser.SeñaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiseñaDef" ):
                return visitor.visitMultiseñaDef(self)
            else:
                return visitor.visitChildren(self)


    class UniseñaDefContext(SeñaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.SeñaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(hinnerParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniseñaDef" ):
                return visitor.visitUniseñaDef(self)
            else:
                return visitor.visitChildren(self)



    def seña(self):

        localctx = hinnerParser.SeñaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_seña)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = hinnerParser.UniseñaDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(hinnerParser.VARIABLE)
                pass

            elif la_ == 2:
                localctx = hinnerParser.MultiseñaDefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(hinnerParser.VARIABLE)
                self.state = 40
                self.match(hinnerParser.T__4)
                self.state = 41
                self.seña()
                pass


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


    class PlusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusExpr" ):
                return visitor.visitPlusExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = hinnerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = hinnerParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(hinnerParser.NUMBER)
                pass
            elif token in [11]:
                localctx = hinnerParser.VariableExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(hinnerParser.VARIABLE)
                pass
            elif token in [6]:
                localctx = hinnerParser.PlusExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(hinnerParser.T__5)
                pass
            elif token in [7]:
                localctx = hinnerParser.LambdaExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.lambda_()
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
        def application(self):
            return self.getTypedRuleContext(hinnerParser.ApplicationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaDef" ):
                return visitor.visitLambdaDef(self)
            else:
                return visitor.visitChildren(self)



    def lambda_(self):

        localctx = hinnerParser.LambdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lambda)
        try:
            localctx = hinnerParser.LambdaDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(hinnerParser.T__6)
            self.state = 51
            self.match(hinnerParser.VARIABLE)
            self.state = 52
            self.match(hinnerParser.T__4)
            self.state = 53
            self.application(0)
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

        def application(self):
            return self.getTypedRuleContext(hinnerParser.ApplicationContext,0)

        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplicationDef" ):
                return visitor.visitApplicationDef(self)
            else:
                return visitor.visitChildren(self)


    class ExprDefContext(ApplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ApplicationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hinnerParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprDef" ):
                return visitor.visitExprDef(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ApplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.ApplicationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def application(self):
            return self.getTypedRuleContext(hinnerParser.ApplicationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)



    def application(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hinnerParser.ApplicationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_application, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = hinnerParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 56
                self.match(hinnerParser.T__7)
                self.state = 57
                self.application(0)
                self.state = 58
                self.match(hinnerParser.T__8)
                pass
            elif token in [6, 7, 10, 11]:
                localctx = hinnerParser.ExprDefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hinnerParser.ApplicationDefContext(self, hinnerParser.ApplicationContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                    self.state = 63
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 64
                    self.expr() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.application_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def application_sempred(self, localctx:ApplicationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




