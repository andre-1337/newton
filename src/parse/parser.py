from syntaxtree.trait import Trait
from syntaxtree.field import Field
from errors.errorcodes import Error
from tokens.tokens import TokenType
from syntaxtree.var import Variable
from syntaxtree._import import Import
from syntaxtree.program import Program
from syntaxtree.function import Function
from syntaxtree.parameter import Parameter
from syntaxtree.reference import Reference
from syntaxtree._struct import Structure, New
from newtcache.cache import Cache, CacheImport
from syntaxtree.controlflow import Break, Continue, Return, If
from syntaxtree.iteration import For, While
from analysis.types import IntTy, FloatTy, VoidTy, StringTy, PointerTy

class Parser:
	def __init__(self, tokens, filename):
		self.tokens = tokens
		self.index = 0
		self.filename = filename
		self.cache = Cache()

	def parse(self):
		statements = []

		while not self.atEnd():
			statements.append(self.statements())
		
		Program(statements)
	
	def match(self, *types):
		for i in types:
			if self.check(i):
				self.advance()
				return True
		
		return False

	def check(self, type):
		if self.atEnd(): return False
		return self.peek().ttype == type

	def statements(self):
		x = None
		if self.match(TokenType.LET):
			x = self.variable()
		elif self.match(TokenType.FN):
			x = self.function("fn")
		elif self.match(TokenType.STRUCT):
			x = self.struct()
		elif self.match(TokenType.TRAIT):
			x = self.trait()
		elif self.match(TokenType.IMPORT):
			x = self._import()
		elif self.match(TokenType.FROM):
			x = self._import("from")
		else:
			x = self.statement()
		
		self.synchronize()

		return x

	def variable(self, assign=False):
		"""let <VariableName>: [modifiers] <type> [= expression];"""
		name = self.consume(TokenType.IDENTIFIER, "Expected a variable identifier.")
		self.consume(TokenType.COLON, "Expected ':' after variable name.")

		modifiers = self.modifiers()
		_type = self._type()
		
		value = None
		if assign:
			self.consume(TokenType.EQ, "Expected '=' after variable type")
			value = self.expression()
		else:
			if self.match(TokenType.EQ):
				value = self.expression()
		
		self.consume(TokenType.SEMICOLON, "Expected ';' after variable declaration.")

		return Variable(name, _type, modifiers, value)

	def modifiers(self):
		modifiers = []
		if self.match(TokenType.ABSTRACT):
			modifiers.append(TokenType.ABSTRACT)
		if self.match(TokenType.MUT):
			modifiers.append(TokenType.MUT)
		if self.match(TokenType.EXTERN):
			modifiers.append(TokenType.EXTERN)
		if self.match(TokenType.VOLATILE):
			modifiers.append(TokenType.VOLATILE)
		if self.match(TokenType.INLINE):
			modifiers.append(TokenType.INLINE)
		if self.match(TokenType.REGISTER):
			modifiers.append(TokenType.REGISTER)

		return modifiers
	
	def _type(self):
		pointer = [False, 0]
		ref = [False, 0]
		if self.match(TokenType.STAR):
			pointer = [True, 1]
			if self.match(TokenType.STAR):
				pointer = [True, 2]

		elif self.match(TokenType.AMPERSAND):
			ref = [True, 1]
			if self.match(TokenType.AMPERSAND):
				ref = [True, 2]
		
		typename = self.consume(TokenType.IDENTIFIER, "Expected type name")
		
		if pointer[0]:
			return PointerTy(typename, pointer[1])
		elif ref[0]:
			return PointerTy(typename, ref[1])
		else:
			return typename

	def params(self):
		params = []

		if not self.match(TokenType.RPAREN):
			params.append(self.parameter())
			while self.match(TokenType.COMMA):
				params.append(self.parameter())
	
	def parameter(self):
		name = self.consume(TokenType.IDENTIFIER, "Expected parameter name.")

		optional = False
		if self.match(TokenType.QUESTION):
			optional = True

		self.consume(TokenType.COLON, "Expected ':' after parameter name.")
		_type = self._type()
		return Parameter(name, _type, optional)
	
	def function(self, kind):
		name = self.consume(TokenType.IDENTIFIER, "Expected function name.")
		generic_params = self.genericParams()
		self.consume(TokenType.LPAREN, "Expected '(' after function name.")

		params = self.params()

		self.consume(TokenType.COLON, "Expected ':' after closing ')'.")

		modifiers = self.modifiers()
		_type = self._type()

		if self.match(TokenType.ARROW):
			body = self.expression()
		else:
			self.consume(TokenType.LBRACE, "Expected '{' after function typename.")
			body = self.block()

		return Function(modifiers, name, params, _type, body, kind)

	def struct(self):
		name = self.consume(TokenType.IDENTIFIER, "Expected struct name.")
		generic_params = self.genericParams()
		
		implements = False
		traits = []
		if self.match(TokenType.IMPLEMENTS):
			implements = True
			traits.append(Reference(self.consume(TokenType.IDENTIFIER, "Expected trait name")))
			while self.match(TokenType.COMMA):
				traits.append(Reference(self.consume(TokenType.IDENTIFIER, "Expected trait name"))) 
					
		
		self.consume(TokenType.LBRACE, "Expected '{' before struct body.")
		body = self.structBody()

		return Structure(name, generic_params != [], generic_params, body[0], body[1], traits, body)
	
	def genericParams(self):
		out = []
		if self.match(TokenType.LBRACKET):
			if not self.match(TokenType.RBRACKET):
				out.append(self.genericParam())
				while self.match(TokenType.COMMA):
					out.append(self.genericParam())
		else:
			return []
	
	def genericParam(self):
		return self.consume(TokenType.IDENTIFIER, "Expected type name.")

	def trait(self):
		name = self.consume(TokenType.IDENTIFIER, "Expected trait name")
		generic_params = self.genericParams()
		self.consume(TokenType.LBRACE, "Expected '{' after trait name")
		body = self.structBody()
		return Trait(name, generic_params, body)
		
	
	def _import(self, kind = ""):
		if kind == "from":
			path = self.expression()
			self.consume(TokenType.IMPORT, "Expected 'import' after import path")
			objs = []
			objs.append(Reference(self.consume(TokenType.IDENTIFIER, "Expected object name")))
			while self.match(TokenType.COMMA):
				objs.append(Reference(self.consume(TokenType.IDENTIFIER, "Expected object name")))
			
			self.consume(TokenType.SEMICOLON, "Expected ';' after import statement")
			
			return Import(path, objects=objs)
		else:
			path = self.expression()
			alias = None
			if self.match(TokenType.AS):
				alias = self.consume(TokenType.IDENTIFIER, "Expected alias name after import path")
			
			return Import(path, alias)

	def structBody(self):
		fields = []
		methods = []

		if self.match(TokenType.FN): 
			methods.append(self.function("method"))

		if self.match(TokenType.IDENTIFIER):
			name = self.previous()
			self.consume(TokenType.COLON, "Expected ':' after field name.")

			modifiers = self.modifiers()
			_type = self._type()

			self.consume(TokenType.SEMICOLON, "Expected ';' after field declaration.")

			fields.append(Field(name, _type, modifiers))


		self.consume(TokenType.RBRACE, "Expected '}' after struct body.")

		return (fields, methods)

	def statement(self):
		if self.match(TokenType.RETURN):
			return self.return_statement()
		elif self.match(TokenType.BREAK):
			return Break()
		elif self.match(TokenType.CONTINUE):
			return Continue()
		elif self.match(TokenType.IF):
			return self.if_statement()
		elif self.match(TokenType.WHILE):
			return self.while_statement()
		elif self.match(TokenType.FOR):
			return self.for_statement()
		elif self.match(TokenType.LBRACE):
			return self.block()
		else:
			return self.expression()

	def return_statement(self):
		if not self.match(TokenType.SEMICOLON):
			return Return(self.expression())
		else:
			return Return(None)

	def if_statement(self):
		self.consume(TokenType.LPAREN, "Expected '(' before if condition")
		condition = self.expression()
		self.consume(TokenType.RPAREN, "Expected ')' after if condition")

		then = self.statement()
		else_ = self.statement() if self.match(TokenType.ELSE) else None
		
		return If(condition, then, else_)


	def while_statement(self):
		self.consume(TokenType.LPAREN, "Expected '(' before while condition")
		condition = self.expression()
		self.consume(TokenType.RPAREN, "Expected ')' after while condition")
		if self.match(TokenType.LBRACE):
			body = self.block()
		else:
			body = self.statement()
		
		return While(condition, body)
	
	def for_statement(self):
		self.consume(TokenType.LPAREN, "Expected '(' before for condition")

		init = None

		if not self.match(TokenType.SEMICOLON):
			init = self.variable(True)
			
	
	def block(self):
		statements = list()

		while not self.match(TokenType.RBRACE) and not self.atEnd():
			statements.append(self.statement())

		return statements
	
	def expression(self):
		...

	def peek(self):
		return self.tokens[self.index]
	
	def atEnd(self):
		return self.index >= len(self.tokens)
	
	def previous(self):
		return self.tokens[self.index-1]
	
	def peekNext(self):
		return self.tokens[self.index+1]
	
	def advance(self):
		self.index += 1
		return self.previous()

	def statements(self):
		pass

	def consume(self, tokenType, message):
		if self.check(tokenType):
			return self.advance()

		Error.printErrorMessage(Error.PARSING_ERROR, message, [ tokenType.line, tokenType.col ], self.filename)
