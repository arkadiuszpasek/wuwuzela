grammar Wuwuzela_Grammar;

MUSIC : 'music' ;
VAR: 'var';
IF: 'if';
COMPOSITION: 'composition';
WRITE: 'write';
TRUE: 'True';
FALSE: 'False';
AND: 'and';
OR: 'or';
WHILE: 'while';
NOT: 'not';
PRINT: 'print';
TRANSPOSE: 'transpose'; 

ASSIGN: '=';
SEMICOLON: ';';
COMMA: ',';
EQUAL: '==';
GREATER: '>';
GREATER_EQUAL: '>=';
LESS: '<';
LESS_EQUAL: '<=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
LBRACKET: '(';
RBRACKET: ')';
LSQUAREBRACKET: '[';
RSQUAREBRACKET: ']';
LBRACE: '{';
RBRACE: '}';

SOUND: [A-G][#]*[b]*([-][1-6])?;
KEY: [a-g][m];
NUMBER: [-]?([0-9]+[.])?[0-9]+;
TEMPO: [1-9][0-9]{1, 2};
VARIABLE: [a-z_][a-zA-Z0-9_]*;
COMMENT: '/*' .*? '*/' -> skip;
STRING: '"'.*?'"';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

musicProgram : MUSIC LBRACE declaration* RBRACE;

declaration: 
     statement
    | varStatement
    ;

statement : 
      whileLoop
    | printStatement
    | ifStatement
    | transposeStatement
    | write
    ;

whileLoop:
 WHILE LBRACKET logicalExpression RBRACKET LBRACE declaration RBRACE;

printStatement:
 PRINT LBRACKET value RBRACKET SEMICOLON;

value: 
    | STRING
    | VARIABLE
    | equation
    ;

ifStatement:
 IF LBRACKET logicalExpression RBRACKET LBRACE declaration RBRACE;

varStatement:
     VAR VARIABLE ASSIGN varStatementContent SEMICOLON;

varStatementContent: 
    SOUND 
| VARIABLE 
| NUMBER 
| logicalExpression 
| containerStatement
;

containerStatement:
 LSQUAREBRACKET containerContent  RSQUAREBRACKET;

containerContent:
 ( SOUND COMMA ) * SOUND;

transposeStatement:
 TRANSPOSE LBRACKET KEY RBRACKET SEMICOLON;

compositionStatement:
 COMPOSITION LBRACKET containerStatement RBRACKET
 | COMPOSITION LBRACKET VARIABLE RBRACKET
 ;

write:
 WRITE LBRACKET STRING COMMA compositionStatement (COMMA TEMPO)? RBRACKET SEMICOLON;

logicalExpression: 
    trueFalse
| logicalExpression andOr logicalExpression 
| equation  comparison equation
| NOT logicalExpression 
| LBRACKET logicalExpression RBRACKET
| element  comparison element
;

andOr: 
    AND
    | OR
    ;

comparison: 
    EQUAL
 | GREATER 
 | GREATER_EQUAL 
 | LESS 
 | LESS_EQUAL
;

equation: 
    element mathOperation element;
element: 
    | VARIABLE
    | NUMBER
    ;

mathOperation: 
    PLUS
    | MINUS
    | DIVIDE
    | MULTIPLY
;

trueFalse:
TRUE 
| FALSE
;




