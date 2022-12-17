from struct import Structure, New
from var import Variable
from array import Array, Subscript
from assign import Assign
from block import Block
from call import Call
from controlflow import Break, Continue, Return, If
from expressions import Binary, Unary, Grouping, Literal
from field import Fields
from function import Function
from _import import Import
from iteration import While, For
from _match import Match
from parameter import Parameter
from program import Program
from reference import Reference, Get, Set
from trait import Trait

class Visitor:
    def visit(self, node):
        method = getattr(self, f"visit{ type(node).__name__ }", None)

        if method is not None:
            return method(node)
        else:
            return node

    def visitProgram(self, node): ... #
    def visitStructureDef(self, node): ... #
    def visitStructureInit(self, node): ... #
    def visitVariable(self, node): ... #
    def visitAssign(self, node): ... #
    def visitParameter(self, node): ... #
    def visitBreak(self, node): ... # 
    def visitContinue(self, node): ... #
    def visitReturn(self, node): ... #
    def visitBinary(self, node): ...#
    def visitUnary(self, node): ...#
    def visitGrouping(self, node): ...#
    def visitCall(self, node): ... #
    def visitGet(self, node): ...#
    def visitSet(self, node): ...#
    def visitIf(self, node): ...#
    def visitWhile(self, node): ...#
    def visitFor(self, node): ...#
    def visitReference(self, node): ...#
    def visitField(self, node): ...#
    def visitTrait(self, node): ...#
    def visitArray(self, node): ...#
    def visitSubscript(self, node): ...#
    def visitBlock(self, node): ...#
    def visitLiteral(self, node): ...#
    def visitImport(self, node): ...#
    def visitFunction(self, node): ... # 
    def visitMatch(self, node): ...#
