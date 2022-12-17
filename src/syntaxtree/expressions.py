class Binary:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def accept(self, visitor):
        return visitor.visitBinary(self)


class Unary:
    def __init__(self, op, right):
        self.op = op
        self.right = right
    
    def accept(self, visitor):
        return visitor.visitUnary(self)


class Literal:
    def __init__(self, value):
        self.value = value
    
    def accept(self, visitor):
        return visitor.visitLiteral(self)


class Grouping:
    def __init__(self, expression):
        self.expression = expression
    
    def accept(self, visitor):
        return visitor.visitGrouping(self)
