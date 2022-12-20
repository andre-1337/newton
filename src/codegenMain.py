"""
A file to test certain codegen aspects of Newton. We want to ensure that the backend is stable and mature enough for whenever we feel like
Newton is ready to be self-hosted.
"""

from codegen.emitter import Emitter
from syntaxtree._struct import Structure

from analysis.types import PointerTy, VoidTy

def main():
	_emit = Emitter("out.c")

	_struct1 = Structure("Pair", True, list([ "T1", "T2" ]), dict({ "key": PointerTy(VoidTy, 1), "value": PointerTy(VoidTy, 1) }), None, None, None)
	_emit.emitStruct(_struct1)

	_struct2 = Structure("SomeReallyComplicatedGenericStruct", True, list([ "A", "B", "C", "D" ]), dict({  }), None, None, None)
	_emit.emitStruct(_struct2)

	_emit.writeFile()

if __name__ == "__main__":
	main()