from sys import exit
from enum import Enum

"""
An enumerator with all the existing tokens in Newton.
"""
class TokenType(Enum):
	# Misc. tokens
	EOF = -1				# eof
	NEWLINE = 0				# \n
	INTEGER = 1				# 123456
	FLOAT = 2				# 123.456
	IDENTIFIER = 3			# foo
	STRING = 4				# "John"
	CHARACTER = 5			# 'c'

	# Operators	
	PLUS = 6				# +
	MINUS = 7				# -
	STAR = 8				# * or **
	SLASH = 9				# /
	PERCENT = 10			# %
	AMPERSAND = 11			# &
	PIPE = 12				# |
	CARET = 13				# ^
	BANG = 14				# !
	QUESTION = 15			# ?
	EQ = 16					# =
	EQEQ = 17				# ==
	NEQ = 18				# !=
	GT = 19					# >
	GTEQ = 20				# >=
	LT = 21					# <
	LTEQ = 22				# <=
	PLUSPLUS = 23			# ++
	MINUSMINUS = 24			# --
	PLUSEQ = 25				# +=
	MINUSEQ = 26			# -=
	STAREQ = 27				# *=
	SLASHEQ = 28			# /=
	PERCENTEQ = 29			# %=
	AMPERSANDEQ = 30		# &=
	PIPEEQ = 31				# |=
	CARETEQ = 32			# ^=
	ARROW = 33				# =>
	DOT = 34				# .
	COLON = 35				# :
	SEMICOLON = 36			# ;
	COMMA = 37				# ,
	LPAREN = 38				# (
	RPAREN = 39				# )
	LBRACE = 40				# {
	RBRACE = 41				# }
	LBRACKET = 42			# [
	RBRACKET = 43			# ]
	GTGT = 44				# >>
	LTLT = 45				# <<
	GTGTEQ = 46				# >>=
	LTLTEQ = 47				# <<=
	

	# Keywords
	LET = 101				# let
	FN = 102				# fn
	IF = 103				# if
	ELSE = 104				# else
	IMPORT = 105			# import
	FROM = 106				# from
	RETURN = 107			# return
	EXTERN = 108			# extern
	WHILE = 109				# while
	TYPE = 110				# type
	STRUCT = 111			# struct
	TRAIT = 112				# trait
	IMPLEMENTS = 113		# implements
	ENUM = 114				# enum
	NEW = 115				# new
	DELETE = 116			# delete
	SIZEOF = 117			# sizeof
	AS = 118				# as
	STATIC = 119			# static
	INLINE = 120			# inline
	ABSTRACT = 121			# abstract
	MUT = 122				# mut
	AND = 123				# and
	OR = 124				# or
	FOR = 125				# for
	BREAK = 126				# break
	CONTINUE = 127			# continue
	TRUE = 128				# true
	FALSE = 129				# false
	NULL = 130				# null
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
	def __init__(self, lexeme, tokenKind, line, col):
		self.lexeme = lexeme
		self.tokenKind = tokenKind
		self.line = line
		self.col = col

	def tokenToStr(self):
		return tokenTypeToStr(self.tokenKind) + " (" + self.lexeme + ")"
