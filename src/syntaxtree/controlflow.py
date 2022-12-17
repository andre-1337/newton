class Break:
    def __init__(self):
        pass

    def visit(self, visitor):
        return visitor.visitBreak(self)
    

class Continue:
    def __init__(self):
        pass

    def visit(self, visitor):
        return visitor.visitContinue(self)


class If:
    def __init__(self, condition, then, else_):
        self.condition = condition
        self.then = then
        self.else_ = else_
    
    def visit(self, visitor):
        return visitor.visitIf(self)


class Return:
    def __init__(self, value = None):
        self.value = value
    
    def visit(self, visitor):
        return visitor.visitReturn(self)
