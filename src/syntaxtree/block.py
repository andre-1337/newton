class Block:
    def __init__(self, statements):
        self.statements = statements
    
    def accept(self, visitor):
        return visitor.visitBlock(self)
