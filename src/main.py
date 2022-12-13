"""
The main driver for the Newton compiler.

This driver takes the input source file, runs it through the lexer, feeds the token stream to the parser,
which in turn feeds the AST output for analysis and then translates Newton source code to C.
"""

from lexer import tokens
from analysis import types
from codegen import emitter
from syntaxtree import struct, var

def main():
	print("Newton compiler")

	_emitter = emitter.Emitter("out.c")

	_struct = struct.Structure("Pair", dict({ "name": types.String() }), dict())

	_str = types.String("\"John Doe\"")
	_var1 = var.Variable("name", _emitter.newtonTypeToC(_str), _str.getValue())

	_uint8 = types.Integer(8, False, 255)
	_var2 = var.Variable("number", _emitter.newtonTypeToC(_uint8), _uint8.getValue())

	_emitter.emitStruct(_struct)
	_emitter.emitVar(_var1)
	_emitter.emitVar(_var2)

	_emitter.emitMain()

	_emitter.writeFile()

	_tkn = tokens.Token(_str.getValue(), tokens.TokenType.STRING)
	print(_tkn.tokenToStr())

if __name__ == "__main__":
	main()