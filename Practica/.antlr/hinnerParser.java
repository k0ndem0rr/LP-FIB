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
		RULE_application = 5, RULE_variable = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "def", "seña", "expr", "lambda", "application", "variable"
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
			setState(29);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(19);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
					case 1:
						{
						setState(14);
						match(T__0);
						}
						break;
					case 2:
						{
						setState(15);
						match(T__1);
						}
						break;
					case 3:
						{
						setState(16);
						application(0);
						}
						break;
					case 4:
						{
						setState(17);
						lambda();
						}
						break;
					case 5:
						{
						setState(18);
						def();
						}
						break;
					}
					setState(24);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__2) {
						{
						{
						setState(21);
						match(T__2);
						}
						}
						setState(26);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					} 
				}
				setState(31);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3526L) != 0)) {
				{
				setState(37);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(32);
					match(T__0);
					}
					break;
				case 2:
					{
					setState(33);
					match(T__1);
					}
					break;
				case 3:
					{
					setState(34);
					application(0);
					}
					break;
				case 4:
					{
					setState(35);
					lambda();
					}
					break;
				case 5:
					{
					setState(36);
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
		public ApplicationContext application() {
			return getRuleContext(ApplicationContext.class,0);
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
			setState(41);
			application(0);
			setState(42);
			match(T__3);
			setState(43);
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
			setState(49);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				_localctx = new UniseñaDefContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(VARIABLE);
				}
				break;
			case 2:
				_localctx = new MultiseñaDefContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				match(VARIABLE);
				setState(47);
				match(T__4);
				setState(48);
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
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
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
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				match(NUMBER);
				}
				break;
			case VARIABLE:
				_localctx = new VariableExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				variable();
				}
				break;
			case T__5:
				_localctx = new PlusExprContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(53);
				match(T__5);
				}
				break;
			case T__6:
				_localctx = new LambdaExprContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(54);
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
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
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
			setState(57);
			match(T__6);
			setState(58);
			variable();
			setState(59);
			match(T__4);
			setState(60);
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
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				{
				_localctx = new ParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(63);
				match(T__7);
				setState(64);
				application(0);
				setState(65);
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
				setState(67);
				expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(74);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ApplicationDefContext(new ApplicationContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_application);
					setState(70);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(71);
					expr();
					}
					} 
				}
				setState(76);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
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

	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ParserRuleContext {
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	 
		public VariableContext() { }
		public void copyFrom(VariableContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableDefContext extends VariableContext {
		public TerminalNode VARIABLE() { return getToken(hinnerParser.VARIABLE, 0); }
		public VariableDefContext(VariableContext ctx) { copyFrom(ctx); }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_variable);
		try {
			_localctx = new VariableDefContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(VARIABLE);
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
		"\u0004\u0001\fP\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0003\u0000\u0014\b\u0000\u0001\u0000\u0005"+
		"\u0000\u0017\b\u0000\n\u0000\f\u0000\u001a\t\u0000\u0005\u0000\u001c\b"+
		"\u0000\n\u0000\f\u0000\u001f\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0003\u0000&\b\u0000\u0003\u0000(\b\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u00022\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u00038\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005E\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0005\u0005I\b\u0005\n\u0005\f\u0005L\t\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0000\u0001\n\u0007\u0000\u0002\u0004\u0006\b\n\f\u0000"+
		"\u0000Y\u0000\u001d\u0001\u0000\u0000\u0000\u0002)\u0001\u0000\u0000\u0000"+
		"\u00041\u0001\u0000\u0000\u0000\u00067\u0001\u0000\u0000\u0000\b9\u0001"+
		"\u0000\u0000\u0000\nD\u0001\u0000\u0000\u0000\fM\u0001\u0000\u0000\u0000"+
		"\u000e\u0014\u0005\u0001\u0000\u0000\u000f\u0014\u0005\u0002\u0000\u0000"+
		"\u0010\u0014\u0003\n\u0005\u0000\u0011\u0014\u0003\b\u0004\u0000\u0012"+
		"\u0014\u0003\u0002\u0001\u0000\u0013\u000e\u0001\u0000\u0000\u0000\u0013"+
		"\u000f\u0001\u0000\u0000\u0000\u0013\u0010\u0001\u0000\u0000\u0000\u0013"+
		"\u0011\u0001\u0000\u0000\u0000\u0013\u0012\u0001\u0000\u0000\u0000\u0014"+
		"\u0018\u0001\u0000\u0000\u0000\u0015\u0017\u0005\u0003\u0000\u0000\u0016"+
		"\u0015\u0001\u0000\u0000\u0000\u0017\u001a\u0001\u0000\u0000\u0000\u0018"+
		"\u0016\u0001\u0000\u0000\u0000\u0018\u0019\u0001\u0000\u0000\u0000\u0019"+
		"\u001c\u0001\u0000\u0000\u0000\u001a\u0018\u0001\u0000\u0000\u0000\u001b"+
		"\u0013\u0001\u0000\u0000\u0000\u001c\u001f\u0001\u0000\u0000\u0000\u001d"+
		"\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000\u001e"+
		"\'\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000 &\u0005"+
		"\u0001\u0000\u0000!&\u0005\u0002\u0000\u0000\"&\u0003\n\u0005\u0000#&"+
		"\u0003\b\u0004\u0000$&\u0003\u0002\u0001\u0000% \u0001\u0000\u0000\u0000"+
		"%!\u0001\u0000\u0000\u0000%\"\u0001\u0000\u0000\u0000%#\u0001\u0000\u0000"+
		"\u0000%$\u0001\u0000\u0000\u0000&(\u0001\u0000\u0000\u0000\'%\u0001\u0000"+
		"\u0000\u0000\'(\u0001\u0000\u0000\u0000(\u0001\u0001\u0000\u0000\u0000"+
		")*\u0003\n\u0005\u0000*+\u0005\u0004\u0000\u0000+,\u0003\u0004\u0002\u0000"+
		",\u0003\u0001\u0000\u0000\u0000-2\u0005\u000b\u0000\u0000./\u0005\u000b"+
		"\u0000\u0000/0\u0005\u0005\u0000\u000002\u0003\u0004\u0002\u00001-\u0001"+
		"\u0000\u0000\u00001.\u0001\u0000\u0000\u00002\u0005\u0001\u0000\u0000"+
		"\u000038\u0005\n\u0000\u000048\u0003\f\u0006\u000058\u0005\u0006\u0000"+
		"\u000068\u0003\b\u0004\u000073\u0001\u0000\u0000\u000074\u0001\u0000\u0000"+
		"\u000075\u0001\u0000\u0000\u000076\u0001\u0000\u0000\u00008\u0007\u0001"+
		"\u0000\u0000\u00009:\u0005\u0007\u0000\u0000:;\u0003\f\u0006\u0000;<\u0005"+
		"\u0005\u0000\u0000<=\u0003\n\u0005\u0000=\t\u0001\u0000\u0000\u0000>?"+
		"\u0006\u0005\uffff\uffff\u0000?@\u0005\b\u0000\u0000@A\u0003\n\u0005\u0000"+
		"AB\u0005\t\u0000\u0000BE\u0001\u0000\u0000\u0000CE\u0003\u0006\u0003\u0000"+
		"D>\u0001\u0000\u0000\u0000DC\u0001\u0000\u0000\u0000EJ\u0001\u0000\u0000"+
		"\u0000FG\n\u0003\u0000\u0000GI\u0003\u0006\u0003\u0000HF\u0001\u0000\u0000"+
		"\u0000IL\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000"+
		"\u0000\u0000K\u000b\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000"+
		"MN\u0005\u000b\u0000\u0000N\r\u0001\u0000\u0000\u0000\t\u0013\u0018\u001d"+
		"%\'17DJ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}