"""
A basic structure in Newton. It is very C-like, but with some added niceties, like being able to declare methods
inside the struct declaration itself. Structs can also be generified, which is helpful to reduce code repetition.
A generified struct gets transpiled to C with the format `structName_genericType`

For example, a Newton struct that declares a pair:

import { println } from std.io;

struct Pair[T1, T2] {
	key: T1;
	value: T2;

	fn new(self: &Self, key: T1, value: T2) -> Pair {
		self.key = key;
		self.value = value;
	}

	fn get_key(self: &Self) -> T1 {
		return self.key;
	}

	fn get_value(self: &Self) -> T2 {
		return self.value;
	}
}

fn main(argc: int, argv: string[]) -> void {
	let pair: Pair[Int, Int] = Pair.new(1, 2);
}

Is turned into the following C:

#include <stdio.h>
#include <stdlib.h>

typedef struct Pair_Int_Int {
	void *T1;
	void *T2;
} Pair_Int_Int;

Pair_Int_Int *Pair_Int_Int_New(void *T1, void *T2) {
	Pair_Int_Int *self = malloc(sizeof(Pair_Int_Int));

	self->T1 = T1;
	self->T2 = T2;

	return self;
}

void *Pair_Int_Int_Get_Key(Pair_Int_Int *self) {
	return self->T1;
}

void *Pair_Int_Int_Get_Value(Pair_Int_Int *self) {
	return self->T2;
}

int main(int argc, char **argv) {
	Pair_Int_Int *pair = Pair_Int_Int_New((void *) 1, (void *) 2);

	printf("%d %d\n", Pair_Int_Int_Get_Key(pair), Pair_Int_Int_Get_Value(pair));

	return 0;
}

"""
class Structure:
	def __init__(self, name, isGeneric, genericParams, fields, methods, traits, body):
		self.name = name
		self.isGeneric = isGeneric
		self.genericParams = genericParams
		self.fields = fields
		self.methods = methods
		self.traits = traits
		self.body = body

		self.mangledCName = self.name

		# mangle the name of the struct so that we can generate generic structs on the C side of things
		if self.isGeneric and self.genericParams is not None:
			for genericParam in self.genericParams:
				self.mangledCName += f"_{ genericParam }"

	def getField(self, fieldName):
		return self.fields[fieldName]

	def getMethod(self, methodName):
		return self.methods[methodName]

	def getTrait(self, traitName):
		return self.traits[traitName]

	def accept(self, visitor):
		return visitor.visitStructDef(self)

class New:
	def __init__(self, structName, parameters):
		self.structName = structName
		self.parameters = parameters
	
	def accept(self, visitor):
		return visitor.visitStructureInit(self)
