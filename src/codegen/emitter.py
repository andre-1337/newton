"""
The emitter for Newton.
This emitter takes the different abstract syntax tree nodes and converts them to C code.
Lots of helper functions help bring the functionality together and makes everything more
maintainable.
"""

from analysis import types

class Emitter:
	def __init__(self, fullPath):
		self.fullPath = fullPath
		self.code = ""

		self.emitIncludes()

	def emit(self, code):
		self.code += code

	def typeSizeToStr(self, ty):
		match ty.getSize():
			case 8:
				return "8"
			
			case 16:
				return "16"

			case 32:
				return "32"

			case 64:
				return "64"
	
	def newtonTypeToC(self, ty):
		match type(ty):
			case types.Integer:
				if ty.getSignedness():
					return "int" + self.typeSizeToStr(ty) + "_t "
				else:
					return "uint" + self.typeSizeToStr(ty) + "_t "

			case types.String:
				return "char *"

			case _:
				pass

	def emitIncludes(self):
		self.emit("#include <stdio.h>\n")
		self.emit("#include <stdlib.h>\n")
		self.emit("#include <stdint.h>\n")

	def emitStruct(self, struct):
		self.emit("typedef struct " + struct.name + " {\n")

		for fieldName in struct.getFields():
			fieldType = self.newtonTypeToC(struct.getFields()[fieldName])
			self.emit(fieldType + "" + fieldName + ";\n")

		self.emit("} " + struct.name + ";\n")

	def emitVar(self, var):
		self.emit(var.type + "" + var.name + " = " + str(var.value) + ";\n")

	def emitMain(self):
		self.emit("int main(int argc, char **argv) {\n")
		self.emit("return 0;\n}\n")

	def writeFile(self):
		with open(self.fullPath, "w") as outputFile:
			outputFile.write(self.code)
