"""
This file contains all the error codes in Newton.
These will be shown in the error messages and you can even look up an error code to know what it is.
"""

from enum import Enum

class ErrorCodes(Enum):
	LEXING_ERROR = 1
	UNTERMINATED_STRING = 2

	@staticmethod
	def __repeat(ch, n):
		return "".join([char * n for char in ch])

	@staticmethod
	def printErrorMessage(errCode, pos, sourceCode, hint = ""):
		result = f"""╭ { ErrorCodes.codeToStr(errCode) } at { pos[0] + 1 }:{ pos[1] + 1 }
┆ { sourceCode[pos[0]] }
┆ { ErrorCodes.__repeat("^", len(sourceCode[pos[0]])) }
"""

		if hint == "":
			pass
		else:
			result += f"┆ Hint: { hint }\n"

		result += "╰━━━━━━━━━━━━━━"
		
		return result

	@staticmethod
	def codeToStr(errCode):
		match errCode:
			case ErrorCodes.LEXING_ERROR:
				return "[ NEWTON-0001 ]: Encountered a lexing error"
			case ErrorCodes.UNTERMINATED_STRING:
				return "[ NEWTON-0002 ]: Encountered an unterminated string literal"
