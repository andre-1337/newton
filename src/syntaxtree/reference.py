class Reference:
    def __init__(self, name, tkn):
        self.name = name
        self.tkn = tkn
    
    def accept(self, visitor):
        return visitor.visitReference(self)


class Get:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj
    
    def accept(self, visitor):
        return visitor.visitGet(self)


class Set:
    def __init__(self, name, obj, value, op):
        self.name = name
        self.obj = obj
        self.value = value
        self.op = op
    
    def accept(self, visitor):
        return visitor.visitSet(self)
