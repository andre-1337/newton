"""
A variable in Newton.
"""

class Variable:
	def __init__(self, name, type, value):
		self.name = name
		self.type = type
		self.value = value

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def getValue(self):
		return self.value
