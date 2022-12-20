class Trait:
    def __init__(self, name, genericParams, body):
        self.name = name
        self.body = body
        self.isGeneric = genericParams != []
        self.genericParams = genericParams
    
    def accept(self, visitor):
        return visitor.visitTrait(self)
