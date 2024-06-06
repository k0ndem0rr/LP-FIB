// Generated from /home/jkonde/Documentos/repos/LP-FIB/Practica/hinner.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class hinnerParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		NUMBER=10, VARIABLE=11, WS=12;
	public static final int
		RULE_root = 0, RULE_def = 1, RULE_seña = 2, RULE_expr = 3, RULE_lambda = 4, 
		RULE_application = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "def", "seña", "expr", "lambda", "application"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\t'", "'\\r'", "'\\n'", "'::'", "'->'", "'(+)'", "'\\'", "'('", 
			"')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "NUMBER", 
			"VARIABLE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "hinner.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public hinnerParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public List<ApplicationContext> application() {
			return getRuleContexts(ApplicationContext.class);
		}
		public ApplicationContext application(int i) {
			return getRuleContext(ApplicationContext.class,i);
		}
		public List<LambdaContext> lambda() {
			return getRuleContexts(LambdaContext.class);
		}
		public LambdaContext lambda(int i) {
			return getRuleContext(LambdaContext.class,i);
		}
		public List<DefContext> def() {
			return getRuleContexts(DefContext.class);
		}
		public DefContext def(int i) {
			return getRuleContext(DefContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(17);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
					case 1:
						{
						setState(12);
						match(T__0);
						}
						break;
					case 2:
						{
						setState(13);
						match(T__1);
						}
						break;
					case 3:
						{
						setState(14);
						application(0);
						}
						break;
					case 4:
						{
						setState(15);
						lambda();
						}
						break;
					case 5:
						{
						setState(16);
						def();
						}
						break;
					}
					setState(19);
					match(T__2);
					}
					} 
				}
				setState(24);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3526L) != 0)) {
				{
				setState(30);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(25);
					match(T__0);
					}
					break;
				case 2:
					{
					setState(26);
					match(T__1);
					}
					break;
				case 3:
					{
					setState(27);
					application(0);
					}
					break;
				case 4:
					{
					setState(28);
					lambda();
					}
					break;
				case 5:
					{
					setState(29);
					def();
					}
					break;
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefContext extends ParserRuleContext {
		public DefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_def; }
	 
		public DefContext() { }
		public void copyFrom(DefContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DefDefContext extends DefContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public SeñaContext seña() {
			return getRuleContext(SeñaContext.class,0);
		}
		public DefDefContext(DefContext ctx) { copyFrom(ctx); }
	}

	public final DefContext def() throws RecognitionException {
		DefContext _localctx = new DefContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_def);
		try {
			_localctx = new DefDefContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			expr();
			setState(35);
			match(T__3);
			setState(36);
			seña();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SeñaContext extends ParserRuleContext {
		public SeñaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seña; }
	 
		public SeñaContext() { }
		public void copyFrom(SeñaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiseñaDefContext extends SeñaContext {
		public TerminalNode VARIABLE() { return getToken(hinnerParser.VARIABLE, 0); }
		public SeñaContext seña() {
			return getRuleContext(SeñaContext.class,0);
		}
		public MultiseñaDefContext(SeñaContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UniseñaDefContext extends SeñaContext {
		public TerminalNode VARIABLE() { return getToken(hinnerParser.VARIABLE, 0); }
		public UniseñaDefContext(SeñaContext ctx) { copyFrom(ctx); }
	}

	public final SeñaContext seña() throws RecognitionException {
		SeñaContext _localctx = new SeñaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_seña);
		try {
			setState(42);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				_localctx = new UniseñaDefContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				match(VARIABLE);
				}
				break;
			case 2:
				_localctx = new MultiseñaDefContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(VARIABLE);
				setState(40);
				match(T__4);
				setState(41);
				seña();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableExprContext extends ExprContext {
		public TerminalNode VARIABLE() { return getToken(hinnerParser.VARIABLE, 0); }
		public VariableExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LambdaExprContext extends ExprContext {
		public LambdaContext lambda() {
			return getRuleContext(LambdaContext.class,0);
		}
		public LambdaExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberExprContext extends ExprContext {
		public TerminalNode NUMBER() { return getToken(hinnerParser.NUMBER, 0); }
		public NumberExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PlusExprContext extends ExprContext {
		public PlusExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expr);
		try {
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(44);
				match(NUMBER);
				}
				break;
			case VARIABLE:
				_localctx = new VariableExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(45);
				match(VARIABLE);
				}
				break;
			case T__5:
				_localctx = new PlusExprContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(46);
				match(T__5);
				}
				break;
			case T__6:
				_localctx = new LambdaExprContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(47);
				lambda();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LambdaContext extends ParserRuleContext {
		public LambdaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lambda; }
	 
		public LambdaContext() { }
		public void copyFrom(LambdaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LambdaDefContext extends LambdaContext {
		public TerminalNode VARIABLE() { return getToken(hinnerParser.VARIABLE, 0); }
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public LambdaDefContext(LambdaContext ctx) { copyFrom(ctx); }
	}

	public final LambdaContext lambda() throws RecognitionException {
		LambdaContext _localctx = new LambdaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_lambda);
		try {
			_localctx = new LambdaDefContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(T__6);
			setState(51);
			match(VARIABLE);
			setState(52);
			match(T__4);
			setState(53);
			application(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ApplicationContext extends ParserRuleContext {
		public ApplicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_application; }
	 
		public ApplicationContext() { }
		public void copyFrom(ApplicationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ApplicationDefContext extends ApplicationContext {
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ApplicationDefContext(ApplicationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprDefContext extends ApplicationContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprDefContext(ApplicationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenthesisContext extends ApplicationContext {
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
		}
		public ParenthesisContext(ApplicationContext ctx) { copyFrom(ctx); }
	}

	public final ApplicationContext application() throws RecognitionException {
		return application(0);
	}

	private ApplicationContext application(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ApplicationContext _localctx = new ApplicationContext(_ctx, _parentState);
		ApplicationContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_application, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				{
				_localctx = new ParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(56);
				match(T__7);
				setState(57);
				application(0);
				setState(58);
				match(T__8);
				}
				break;
			case T__5:
			case T__6:
			case NUMBER:
			case VARIABLE:
				{
				_localctx = new ExprDefContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(60);
				expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(67);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ApplicationDefContext(new ApplicationContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_application);
					setState(63);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(64);
					expr();
					}
					} 
				}
				setState(69);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 5:
			return application_sempred((ApplicationContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean application_sempred(ApplicationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\fG\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0003\u0000\u0012\b\u0000\u0001\u0000\u0005\u0000\u0015\b\u0000"+
		"\n\u0000\f\u0000\u0018\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0003\u0000\u001f\b\u0000\u0003\u0000!\b\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002+\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u00031\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005>\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0005\u0005B\b\u0005\n\u0005\f\u0005E\t\u0005\u0001\u0005\u0000"+
		"\u0001\n\u0006\u0000\u0002\u0004\u0006\b\n\u0000\u0000P\u0000\u0016\u0001"+
		"\u0000\u0000\u0000\u0002\"\u0001\u0000\u0000\u0000\u0004*\u0001\u0000"+
		"\u0000\u0000\u00060\u0001\u0000\u0000\u0000\b2\u0001\u0000\u0000\u0000"+
		"\n=\u0001\u0000\u0000\u0000\f\u0012\u0005\u0001\u0000\u0000\r\u0012\u0005"+
		"\u0002\u0000\u0000\u000e\u0012\u0003\n\u0005\u0000\u000f\u0012\u0003\b"+
		"\u0004\u0000\u0010\u0012\u0003\u0002\u0001\u0000\u0011\f\u0001\u0000\u0000"+
		"\u0000\u0011\r\u0001\u0000\u0000\u0000\u0011\u000e\u0001\u0000\u0000\u0000"+
		"\u0011\u000f\u0001\u0000\u0000\u0000\u0011\u0010\u0001\u0000\u0000\u0000"+
		"\u0012\u0013\u0001\u0000\u0000\u0000\u0013\u0015\u0005\u0003\u0000\u0000"+
		"\u0014\u0011\u0001\u0000\u0000\u0000\u0015\u0018\u0001\u0000\u0000\u0000"+
		"\u0016\u0014\u0001\u0000\u0000\u0000\u0016\u0017\u0001\u0000\u0000\u0000"+
		"\u0017 \u0001\u0000\u0000\u0000\u0018\u0016\u0001\u0000\u0000\u0000\u0019"+
		"\u001f\u0005\u0001\u0000\u0000\u001a\u001f\u0005\u0002\u0000\u0000\u001b"+
		"\u001f\u0003\n\u0005\u0000\u001c\u001f\u0003\b\u0004\u0000\u001d\u001f"+
		"\u0003\u0002\u0001\u0000\u001e\u0019\u0001\u0000\u0000\u0000\u001e\u001a"+
		"\u0001\u0000\u0000\u0000\u001e\u001b\u0001\u0000\u0000\u0000\u001e\u001c"+
		"\u0001\u0000\u0000\u0000\u001e\u001d\u0001\u0000\u0000\u0000\u001f!\u0001"+
		"\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000 !\u0001\u0000\u0000"+
		"\u0000!\u0001\u0001\u0000\u0000\u0000\"#\u0003\u0006\u0003\u0000#$\u0005"+
		"\u0004\u0000\u0000$%\u0003\u0004\u0002\u0000%\u0003\u0001\u0000\u0000"+
		"\u0000&+\u0005\u000b\u0000\u0000\'(\u0005\u000b\u0000\u0000()\u0005\u0005"+
		"\u0000\u0000)+\u0003\u0004\u0002\u0000*&\u0001\u0000\u0000\u0000*\'\u0001"+
		"\u0000\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,1\u0005\n\u0000\u0000"+
		"-1\u0005\u000b\u0000\u0000.1\u0005\u0006\u0000\u0000/1\u0003\b\u0004\u0000"+
		"0,\u0001\u0000\u0000\u00000-\u0001\u0000\u0000\u00000.\u0001\u0000\u0000"+
		"\u00000/\u0001\u0000\u0000\u00001\u0007\u0001\u0000\u0000\u000023\u0005"+
		"\u0007\u0000\u000034\u0005\u000b\u0000\u000045\u0005\u0005\u0000\u0000"+
		"56\u0003\n\u0005\u00006\t\u0001\u0000\u0000\u000078\u0006\u0005\uffff"+
		"\uffff\u000089\u0005\b\u0000\u00009:\u0003\n\u0005\u0000:;\u0005\t\u0000"+
		"\u0000;>\u0001\u0000\u0000\u0000<>\u0003\u0006\u0003\u0000=7\u0001\u0000"+
		"\u0000\u0000=<\u0001\u0000\u0000\u0000>C\u0001\u0000\u0000\u0000?@\n\u0003"+
		"\u0000\u0000@B\u0003\u0006\u0003\u0000A?\u0001\u0000\u0000\u0000BE\u0001"+
		"\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000"+
		"D\u000b\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000\b\u0011\u0016"+
		"\u001e *0=C";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}