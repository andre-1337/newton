class Function:
    def __init__(self, modifiers, name, parameters, returnType, body):
        self.modifiers = modifiers
        self.name = name
        self.parameters = parameters
        self.returnType = returnType
        self.body = body
    
    def visit(self, visitor):
        visitor.visitFunction(self)
