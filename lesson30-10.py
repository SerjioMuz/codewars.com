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

class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:' , pargs, kargs)

class Prog:
    def __init__(self, value):
        self.value=value
    def __call__(self, other):
        return self.value * other

class Prog:
    def __init__(self, value):
        self.value=value
    def comp(self, other):
        return self.value * other

class Callback:
    def __init__(self, color):
        self.color=color
    def __call__(self):
        print('turn', self.color)

def callback(color):
    def oncall():
        print('turn', color)
    return oncall

class C:
    data='spam'
    def __gt__(self, other):
        return self.data>other
    def __lt__(self, other):
        return self.data<other
