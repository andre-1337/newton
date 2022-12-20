"""
This file contains all the possible types within Newton
"""

class UserDefinedTy:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"""{ self.name } """

class IntTy:
	def __init__(self, size, signed):
		self.size = size
		self.signed = signed

	def __str__(self):
		return f""""""

class FloatTy:
	pass

class StringTy:
	pass

class VoidTy:
	def __init__(self):
		pass

	def __str__(self):
		return "void"

class PointerTy:
	def __init__(self, baseTy, n):
		self.baseTy = baseTy
		self.n = n

	def __str__(self):
		return f"""{ "*" * self.n }{ self.baseTy.__str__(self) } """

class ArrayTy:
	def __init__(self, ty, size):
		self.ty = ty
		self.size = size

	def __str__(self):
		res = ""

		if self.size is None:
			res = f"""[?]{ self.ty } """
		else:
			res = f"""[{ self.size }]{ self.ty } """

		return res
