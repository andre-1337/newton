class Parameter:
    def __init__(self, name, ttype, modifiers, optional=False):
        self.name = name
        self.type = ttype
        self.modifiers = modifiers
        self.optional = optional
    
    def accept(self, visitor):
        visitor.visitParameter(self)
