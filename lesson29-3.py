"""class Super:
    def hello(self):
        self.data1='spam'

class Sub(Super):
    def hola(self):
        self.data2='eggs'"""

def classtree(cls, indent):
    print('.' * indent +cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent+3)

def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__': selftest()


"I am: docstr.__doc__"
def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am:spam.method.__doc__ or self.methob.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)
