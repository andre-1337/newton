from sys import exit
from enum import Enum

"""
An enumerator with all the existing tokens in Newton.
"""
class TokenType(Enum):
	# Misc. tokens
	EOF = -1			# eof
	NEWLINE = 0			# \n
	INTEGER = 1			# 123456
	FLOAT = 2			# 123.456
	IDENTIFIER = 3		# foo
	STRING = 4			# "John"
	CHARACTER = 5		# 'c'

	# Keywords
	LET = 101			# let
	FN = 102			# fn
	IF = 103			# if
	ELSE = 104			# else
	IMPORT = 105		# import
	FROM = 106			# from
	RETURN = 107		# return
	EXTERN = 108		# extern
	WHILE = 109			# while
	TYPE = 110			# type
	STRUCT = 111		# struct
	TRAIT = 112			# trait
	IMPLEMENTS = 113	# implements
	ENUM = 114			# enum
	NEW = 115			# new
	DELETE = 116		# delete
	SIZEOF = 117		# sizeof
	AS = 118			# as
	STATIC = 119		# static
	INLINE = 120		# inline
	ABSTRACT = 121		# abstract
	MUT = 122			# mut

	# Operators

def tokenTypeToStr(tokenKind):
	match tokenKind:
		case TokenType.EOF:
			return "<eof>"

		case TokenType.NEWLINE:
			return "<newline>"

		case TokenType.INTEGER:
			return "<int>"

		case TokenType.FLOAT:
			return "<float>"

		case TokenType.IDENTIFIER:
			return "<identifier>"

		case TokenType.STRING:
			return "<string>"

		case TokenType.CHAR:
			return "<char>"

		case _:
			exit("how did you even get here?")

"""
A class that represents a token in Newton.
"""
class Token:
	def __init__(self, tokenText, tokenKind):
		self.tokenText = tokenText
		self.tokenKind = tokenKind

	def tokenToStr(self):
		return tokenTypeToStr(self.tokenKind) + " (" + self.tokenText + ")"
