class Parameter:
    def __init__(self, name, ttype, optional=False):
        self.name = name
        self.type = ttype
        self.optional = optional
    
    def accept(self, visitor):
        visitor.visitParameter(self)
