/*
 A scanner for a Anaconda integers. Outputs lines like
 "token: lexeme", for example "decimal_integer: +12".
*/

%option noyywrap

%{

%}

/* your definitions go here */

%%
/* Decimal Numbers */
^[-+]?[0]$  			printf("decimal_int: ", yytext);
^[-+]?[1-9]?[0-9]*$  		printf("decimal_int: ", yytext);

/* Hexadecimal Numbers */
^[-+]?[xX]?[0]$			printf("hexadecimal_int: ", yytext);
^[-+]?[xX]?[1-9][0-9]*$		printf("hexadecimal_int: ", yytext);

/* Octal Numbers */
^[-+]?[0]?[0]$			printf("octal_int: ", yytext);
^[-+]?[0]?[1-7][0-7]*$		printf("octal_int: ", yytext);
%%

/* your rules go here */

"#".*\n               printf("COMMENT: %s", yytext);
[ \t\n]+              /* skip space, tab and newline */
.                     printf("ignore: %s\n", yytext);

%%

main(argc, argv)
  int argc; char **argv;
  { 
    if (argc>1) yyin=fopen(argv[1],"r"); else yyin=stdin;
    yylex();
  }

