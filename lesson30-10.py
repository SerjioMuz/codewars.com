class Number:
    def __init__(self, val):
        self.val=val
    def __iadd__(self, other):
        self.val+=other
        return self


