from syntaxtree import Visitor
from errors.errorcodes import Error

class Parser:
	def __init__(self, tokens, filename):
		self.tokens = tokens
		self.filename = filename

	def parse(self):
		statements = []

	def statements(self):
		pass

	def consume(self, tokenType, message):
		if self.check(tokenType):
			return self.advance()

		Error.printErrorMessage(Error.PARSING_ERROR, f"Expected " [ 0, 0 ], self.filename)
