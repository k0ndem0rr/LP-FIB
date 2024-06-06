grammar hinner;

// 2
// x
// (+) 2
// \x -> (+) 2 x
// (\x -> (+) 2 x) 4

root : 
    expr+
    ;

expr :
    NUMBER                  # numberExpr
    | VARIABLE              # variableExpr
    | '(+)' NUMBER    # addExpr
    | lambda                # lambdaExpr 
    | application           # applicationExpr
    ;

lambda : 
    '\\' VARIABLE '->' expr #lambdaDef
    ;
application : 
    '(' lambda expr ')'     #applicationDef
    ;


NUMBER     : [0-9]+ ;
VARIABLE   : [a-zA-Z]+ ;
WS         : [ \t\r\n]+ -> skip ;

