"""
The main driver for the Newton compiler.

This driver takes the input source file, runs it through the lexer, feeds the token stream to the parser,
which in turn feeds the AST output for analysis and then translates Newton source code to C.
"""

from sys import argv, exit

from lexer.lexer import Lexer
from tokens.tokens import TokenType

def main():
	if (len(argv) != 2):
		print("The Newton compiler requires a source file as an input")
		exit(-1)
	else:
		_lex = Lexer(argv[1])
		
		tokens = _lex.lex()
		for t in tokens:
			print(str(t))
if __name__ == "__main__":
	main()