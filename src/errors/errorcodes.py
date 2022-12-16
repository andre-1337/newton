"""
This file contains all the error codes in Newton.
These will be shown in the error messages and you can even look up an error code to know what it is.
"""

from sys import exit
from enum import Enum

class ErrorCodes(Enum):
	INTERNAL_ERROR = 0
	LEXING_ERROR = 1
	UNTERMINATED_STRING = 2

	@staticmethod
	def printErrorMessage(errCode, pos, filename, hint = ""):
		lineAtFault = open(filename, "r").readlines()[pos[0]-1][pos[1]]
		
		result = f"""╭ { ErrorCodes.codeToStr(errCode) } at { pos[0] }:{ pos[1] }
┆
┆ { lineAtFault }
┆ { "^" * len(lineAtFault) }
┆
"""

		if hint == "":
			pass
		else:
			result += f"┆ Hint: { hint }\n"

		result += "╰━━━━━━━━━━━━━━\n"
		
		print(result)
		exit(-1)

	@staticmethod
	def codeToStr(errCode):
		match errCode:
			case ErrorCodes.INTERNAL_ERROR:
				return "[ NEWTON-0000 ]: Ooops! You ran into an internal compiler error"
			case ErrorCodes.LEXING_ERROR:
				return "[ NEWTON-0001 ]: Encountered a lexing error"
			case ErrorCodes.UNTERMINATED_STRING:
				return "[ NEWTON-0002 ]: Encountered an unterminated string literal"

			case _:
				return "how did you get here?"
