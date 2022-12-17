"""
A variable in Newton.
"""

class Variable:
	def __init__(self, name, type, modifiers, value = None):
		self.name = name
		self.type = type
		self.value = value
		self.modifiers = modifiers

	def accept(self, visitor):
		return visitor.visitVariable(self)