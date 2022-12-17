class Match:
    def __init__(self, cases, default=None, _finally=None):
        self.cases = cases
        self.default = default
        self._finally = _finally
    
    def accept(self, visitor):
        return visitor.visitMatch(self)
