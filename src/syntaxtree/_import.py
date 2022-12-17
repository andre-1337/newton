class Import:
    def __init__(self, path, alias=None, objects=None):
        self.path = path
        self.alias = alias
        self.objects = objects
    
    def accept(self, visitor):
        visitor.visitImport(self)
