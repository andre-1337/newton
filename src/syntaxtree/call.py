class Call:
    def __init__(self, paren, callee, args):
        self.paren = paren
        self.callee = callee
        self.args = args
    
    def accept(self, visitor):
        return visitor.visitCall(self)
