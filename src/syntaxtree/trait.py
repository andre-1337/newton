class Trait:
    def __init__(self, name, modifiers, body):
        self.name = name
        self.body = body
        self.modifiers = modifiers
    
    def accept(self, visitor):
        return visitor.visitTrait(self)
