class Assign:
    def __init__(self, name, op, value):
        self.name = name
        self.op = op
        self.value = value
    
    def accept(self, visitor):
        return visitor.visitAssign(self)