class Program:
    def __init__(self, statements):
        self.statements = statements
    
    def accept(self, visitor):
        visitor.visitProgram(self)
