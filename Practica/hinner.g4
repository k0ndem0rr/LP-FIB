grammar hinner;

root : 
    (('\t'|'\r'|application|lambda|def) '\n')* 
    (('\t'|'\r'|application|lambda|def))? 
    ;
def:
    expr '::' seña #defDef
    ;

seña:
    VARIABLE #uniseñaDef
    | VARIABLE '->' seña #multiseñaDef
    ;

expr :
    NUMBER                  # numberExpr
    | VARIABLE              # variableExpr
    | '(+)'                 # plusExpr
    | lambda                # lambdaExpr 
    ;

lambda : 
    '\\' VARIABLE '->' application #lambdaDef
    ;
application : 
    application expr      #applicationDef
    | '(' application ')'  #parenthesis
    | expr                 #exprDef
    ;


NUMBER     : [0-9]+ ;
VARIABLE   : [a-zA-Z]+ ;
WS         : [ \t\r\n]+ -> skip ;

