class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    
    def visit(self, visitor):
        return visitor.visitWhile(self)


class For:
    def __init__(self, init, condition, step, body):
        self.init = init
        self.condition = condition
        self.step = step
        self.body = body
    
    def visit(self, visitor):
        return visitor.visitFor(self)
