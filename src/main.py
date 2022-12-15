"""
The main driver for the Newton compiler.

This driver takes the input source file, runs it through the lexer, feeds the token stream to the parser,
which in turn feeds the AST output for analysis and then translates Newton source code to C.
"""

from lexer import tokens
from analysis import types
from codegen import emitter
from errors import errorcodes
from syntaxtree import struct, var

def sourceToArr(source):
	return source.split("\n")

def main():
	print("Newton compiler")

	_str = types.String("Hello, world!")

	_tkn = tokens.Token(_str.getValue(), tokens.TokenType.STRING, 3, len(_str.getValue()))

	_err = errorcodes.ErrorCodes.UNTERMINATED_STRING
	_src = sourceToArr("from std.io import println;\n\nfn main(argc: int, argv: string[]): int {\n    println(\"Hello, world!);\n	return 0;\n}")

	_errStr = errorcodes.ErrorCodes.printErrorMessage(_err, [ _tkn.line, _tkn.col ], _src, "Consider closing the string with \"")	

	print(_errStr) 

if __name__ == "__main__":
	main()