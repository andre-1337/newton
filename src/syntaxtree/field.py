class Field:
    def __init__(self, name, type, modifiers):
        self.name = name
        self.type = type
        self.modifiers = modifiers
    
    def accept(self, visitor):
        return visitor.visitField(self)
