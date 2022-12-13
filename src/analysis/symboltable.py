"""
Newton's symbol table. This class keeps track of all the declared variables, enumerators, structures, functions and others.
"""

class SymbolTable:
	def __init__(self):
		self.variables = dict()
		self.enumerators = dict()
		self.structures = dict()
		self.functions = dict()

	def addVariable(self, var):
		self.variables[var.getName()] = var

	def addEnumerator(self, enum):
		self.enumerators[enum.getName()] = enum

	def addStructure(self, struct):
		self.structures[struct.getName()] = struct

	def addFunction(self, fn):
		self.functions[fn.getName()] = fn