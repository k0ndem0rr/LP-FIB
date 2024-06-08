grammar hinner;

root : 
    (('\t'|'\r'|application|lambda|def) '\n'*)* 
    (('\t'|'\r'|application|lambda|def))? 
    ;
def:
    variable '::' expr      #invalidDef
    | application '::' seña #defDef
    ;

seña:
    VARIABLE                #uniseñaDef
    | VARIABLE '->' seña    #multiseñaDef
    ;

expr :
    NUMBER                  # numberExpr
    | variable              # variableExpr
    | '(+)'                 # plusExpr
    | lambda                # lambdaExpr 
    ;

lambda : 
    '\\' variable '->' application #lambdaDef
    ;
application : 
    application expr        #applicationDef
    | '(' application ')'   #parenthesis
    | expr                  #exprDef
    ;

variable : 
    VARIABLE                #variableDef
    | '(' variable ')'      #variableParenthesis
    ;

NUMBER     : [0-9]+ ;
VARIABLE   : [a-zA-Z]+ ;
WS         : [ \t\r\n]+ -> skip ;

