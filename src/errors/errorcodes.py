"""
This file contains all the error codes in Newton.
These will be shown in the error messages and you can even look up an error code to know what it is.
"""

from sys import exit
from enum import Enum

RED = "\033[1;31m"
RESET = "\033[1;0m"

class Error(Enum):
	INTERNAL_ERROR = 0
	LEXING_ERROR = 1
	PARSING_ERROR = 2
	UNTERMINATED_STRING = 3

	@staticmethod
	def printErrorMessage(errCode, errMessage, pos, filename, hint = ""):
		lineAtFault = open(filename, "r").readlines()[pos[0]-1][pos[1]]
		
		result = f"""╭ { RED }{ Error.codeToStr(errCode) + errMessage}
{ RESET }┆
{ pos[0] }:{ pos[1] } ┆ { lineAtFault }
┆ { " " * (pos[0] - 1) }{ "^" * len(lineAtFault) }
┆
"""

		if hint == "":
			pass
		else:
			result += f"┆ Hint: { hint }\n"

		result += f"╰━━━━━━━━━━━━━━\n"
		
		print(result)
		exit(-1)

	@staticmethod
	def codeToStr(errCode):
		match errCode:
			case Error.INTERNAL_ERROR:
				return "[ NEWTON-0000 ]: "

			case Error.LEXING_ERROR:
				return "[ NEWTON-0001 ]: "

			case Error.PARSING_ERROR:
				return "[ NEWTON-0002 ]: "

			case Error.UNTERMINATED_STRING:
				return "[ NEWTON-0003 ]: "

			case _:
				return "how did you get here?"
