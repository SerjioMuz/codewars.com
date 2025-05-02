class Number:
    def __init__(self, val):
        self.val=val
    def __iadd__(self, other):
        self.val+=other
        return self


class Number:
    def __init__(self, val):
        self.val=val
    def __add__(self, other):
        return Number(self.val+other)
