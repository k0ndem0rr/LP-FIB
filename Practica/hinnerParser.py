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
        4,1,12,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,3,0,20,8,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,
        5,0,28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,0,1,0,1,0,3,0,38,8,0,3,0,40,
        8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,50,8,2,1,3,1,3,1,3,1,3,3,
        3,56,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,69,8,5,
        1,5,1,5,5,5,73,8,5,10,5,12,5,76,9,5,1,6,1,6,1,6,0,1,10,7,0,2,4,6,
        8,10,12,0,0,89,0,29,1,0,0,0,2,41,1,0,0,0,4,49,1,0,0,0,6,55,1,0,0,
        0,8,57,1,0,0,0,10,68,1,0,0,0,12,77,1,0,0,0,14,20,5,1,0,0,15,20,5,
        2,0,0,16,20,3,10,5,0,17,20,3,8,4,0,18,20,3,2,1,0,19,14,1,0,0,0,19,
        15,1,0,0,0,19,16,1,0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,24,1,0,0,
        0,21,23,5,3,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,27,19,1,0,0,0,28,31,1,0,0,0,
        29,27,1,0,0,0,29,30,1,0,0,0,30,39,1,0,0,0,31,29,1,0,0,0,32,38,5,
        1,0,0,33,38,5,2,0,0,34,38,3,10,5,0,35,38,3,8,4,0,36,38,3,2,1,0,37,
        32,1,0,0,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,
        0,38,40,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,1,1,0,0,0,41,42,3,
        10,5,0,42,43,5,4,0,0,43,44,3,4,2,0,44,3,1,0,0,0,45,50,5,11,0,0,46,
        47,5,11,0,0,47,48,5,5,0,0,48,50,3,4,2,0,49,45,1,0,0,0,49,46,1,0,
        0,0,50,5,1,0,0,0,51,56,5,10,0,0,52,56,3,12,6,0,53,56,5,6,0,0,54,
        56,3,8,4,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,
        0,56,7,1,0,0,0,57,58,5,7,0,0,58,59,3,12,6,0,59,60,5,5,0,0,60,61,
        3,10,5,0,61,9,1,0,0,0,62,63,6,5,-1,0,63,64,5,8,0,0,64,65,3,10,5,
        0,65,66,5,9,0,0,66,69,1,0,0,0,67,69,3,6,3,0,68,62,1,0,0,0,68,67,
        1,0,0,0,69,74,1,0,0,0,70,71,10,3,0,0,71,73,3,6,3,0,72,70,1,0,0,0,
        73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,11,1,0,0,0,76,74,1,
        0,0,0,77,78,5,11,0,0,78,13,1,0,0,0,9,19,24,29,37,39,49,55,68,74
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
    RULE_variable = 6

    ruleNames =  [ "root", "def", "seña", "expr", "lambda", "application", 
                   "variable" ]

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
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 19
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 14
                        self.match(hinnerParser.T__0)
                        pass

                    elif la_ == 2:
                        self.state = 15
                        self.match(hinnerParser.T__1)
                        pass

                    elif la_ == 3:
                        self.state = 16
                        self.application(0)
                        pass

                    elif la_ == 4:
                        self.state = 17
                        self.lambda_()
                        pass

                    elif la_ == 5:
                        self.state = 18
                        self.def_()
                        pass


                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 21
                        self.match(hinnerParser.T__2)
                        self.state = 26
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
             
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3526) != 0):
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.match(hinnerParser.T__0)
                    pass

                elif la_ == 2:
                    self.state = 33
                    self.match(hinnerParser.T__1)
                    pass

                elif la_ == 3:
                    self.state = 34
                    self.application(0)
                    pass

                elif la_ == 4:
                    self.state = 35
                    self.lambda_()
                    pass

                elif la_ == 5:
                    self.state = 36
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

        def application(self):
            return self.getTypedRuleContext(hinnerParser.ApplicationContext,0)

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
            self.state = 41
            self.application(0)
            self.state = 42
            self.match(hinnerParser.T__3)
            self.state = 43
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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = hinnerParser.UniseñaDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(hinnerParser.VARIABLE)
                pass

            elif la_ == 2:
                localctx = hinnerParser.MultiseñaDefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(hinnerParser.VARIABLE)
                self.state = 47
                self.match(hinnerParser.T__4)
                self.state = 48
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

        def variable(self):
            return self.getTypedRuleContext(hinnerParser.VariableContext,0)


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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = hinnerParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(hinnerParser.NUMBER)
                pass
            elif token in [11]:
                localctx = hinnerParser.VariableExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.variable()
                pass
            elif token in [6]:
                localctx = hinnerParser.PlusExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(hinnerParser.T__5)
                pass
            elif token in [7]:
                localctx = hinnerParser.LambdaExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 54
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

        def variable(self):
            return self.getTypedRuleContext(hinnerParser.VariableContext,0)

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
            self.state = 57
            self.match(hinnerParser.T__6)
            self.state = 58
            self.variable()
            self.state = 59
            self.match(hinnerParser.T__4)
            self.state = 60
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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = hinnerParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.match(hinnerParser.T__7)
                self.state = 64
                self.application(0)
                self.state = 65
                self.match(hinnerParser.T__8)
                pass
            elif token in [6, 7, 10, 11]:
                localctx = hinnerParser.ExprDefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hinnerParser.ApplicationDefContext(self, hinnerParser.ApplicationContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                    self.state = 70
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 71
                    self.expr() 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hinnerParser.RULE_variable

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableDefContext(VariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hinnerParser.VariableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(hinnerParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDef" ):
                return visitor.visitVariableDef(self)
            else:
                return visitor.visitChildren(self)



    def variable(self):

        localctx = hinnerParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        try:
            localctx = hinnerParser.VariableDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(hinnerParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
         




