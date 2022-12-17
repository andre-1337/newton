class Array:
    def __init__(self, size, elements):
        self.size = size
        self.elements = elements
    
    def accept(self, visitor):
        visitor.visitArray(self)

class Subscript:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index
    
    def accept(self, visitor):
        visitor.visitSubscript(self)
