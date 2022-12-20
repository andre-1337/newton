class Function:
    def __init__(self, modifiers, name, parameters, genericParams, returnType, body, kind):
        self.modifiers = modifiers
        self.name = name
        self.parameters = parameters
        self.isGeneric = genericParams != []
        self.genericParams == genericParams
        self.returnType = returnType
        self.body = body
        self.kind = kind
    
    def visit(self, visitor):
        visitor.visitFunction(self)
