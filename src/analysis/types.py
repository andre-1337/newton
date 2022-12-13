"""
This file contains all the types that exist in Newton
"""

"""
An integer. The size can be anything between 8 to 64. Signed integers can be negative, while unsigned cannot.
"""
class Integer:
	def __init__(self, size, isSigned, value):
		self.size = size
		self.isSigned = isSigned
		self.value = value

	def getSize(self):
		return self.size

	def getSignedness(self):
		return self.isSigned

	def getValue(self):
		return self.value
	
"""
Floating point numbers. The size can be anything between 16 to 64.
"""
class Float:
	def __init__(self, size, value):
		self.size = size
		self.value = value

	def getSize(self):
		return self.size

	def getValue(self):
		return self.value

"""
A string in Newton. Can be internally represented as a pointer of characters, an array of characters (which decays to a pointer)
or a vector of unsigned 8-bit integers
"""
class String:
	def __init__(self, value = ""):
		self.value = value

	def getValue(self):
		return self.value
