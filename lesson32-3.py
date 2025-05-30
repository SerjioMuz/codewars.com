class E:
    __slots__=['a', 'd']

class D(E):
    __slots__=['a', '__dict__']

class Slotful:
    __slots__=['a', 'b', '__dict__']
    def __init__(self, data):
        self.c=data
