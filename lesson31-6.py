class Selfless:
    def __init__(self, data):
        self.data=data
    def selfless(arg1, arg2):
        return arg1+arg2
    def normal(self, arg1, arg2):
        return self.data+arg1+arg2

class Number:
    def __init__(self, base):
        self.base=base
    def double(self):
        return self.base*2
    def triple(self):
        return self.base*3

def sguare(arg):
    return arg**2

class Sum:
    def __init__(self, val):
        self.val=val
    def __call__(self,arg):
        return self.val+arg

class Product:
    def __init__(self, val):
        self.val=val
    def method(self, arg):
        return self.val*arg

class Negate:
    def __init__(self, val):
        self.val=-val
    def __repr__(self):
        return str(self.val)
