
class operators:
    def __getattr__(self, name):
        if name=='age':
            return 40
        else:
            raise AttributeError(name)

class properties(object):
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age=value
    age=property(getage, setage, None, None)

class operators:
    def __getattr__(self, name):
        if name=='age':
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name=='age':
            self.__dict__['_age']=value
        else:
            self.__dict__[name]=value

class AgeDesc(object):
    def __get__(self, instance, owner): return 40
    def __set__(self, instance, value): instance._age=value
class descriptors(object):
    age=AgeDesc()

"Файл spam_class.py"
class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances=Spam.numInstances+1
    def printNumInstances(self):
        print('Number of instances created: %s' % Spam.numInstances)


"Файл bothmethods.py"
class Methods:
    def imeth(self, x):
        print([self, x])
    def smeth(x):
        print([x])
    def cmeth(cls,x):
        print(cls,x)
    smeth=staticmethod(smeth)
    cmeth=classmethod(cmeth)

"Файл spam_static.py"
class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances +=1
    def printNumInstances():
        print('Number of instances: %s' % Spam.numInstances)
    printNumInstances=staticmethod(printNumInstances)
class Sub(Spam):
    def printNumInstances():
        print('Extra stuff...')
        Spam.printNumInstances()
    printNumInstances=staticmethod(printNumInstances)


class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances +=1
    def printNumInstances(cls):
        print('Number of instances: %s %s' % (cls.numInstances, cls))
    printNumInstances=classmethod(printNumInstances)
class Sub(Spam):
    def printNumInstances(cls):
        print('Extra stuff...', cls)
        Spam.printNumInstances()
    printNumInstances=classmethod(printNumInstances)
class Other(Spam): pass


class Spam():
    numInstances = 0
    def count(cls):
        cls.numInstances+=1
    def __init__(self):
        self.count()
    count=classmethod(count)
class Sub(Spam):
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)
class Other(Spam):
    numInstances = 0

class Spam():
    numInstances = 0
    def __init__(self):
        Spam.numInstances=Spam.numInstances + 1
    @staticmethod
    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)


"Файл bothmethods_decorators.py"
class Methods(object):
    def imeth(self, x):
        print([self,x])
    @staticmethod
    def smeth(x):
        print(x)
    @classmethod
    def cmeth(cls, x):
        print([cls, x])
    @property
    def name(self):
        return 'Bob '+self.__class__.__name__


"Файл tracer1.py"
class tracer:
    def __init__(self, func):
        self.calls=0
        self.func=func
    def __call__(self, *args):
        self.calls+=1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)
    @tracer
    def spam(self,a,b,c):
        return a+b+c
x=tracer()
print(x.spam(1,2,3))
print(x.spam('a', 'b', 'c'))


def tracer(func):
    def oncall(*args):
        oncall.calls +=1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls=0
    return oncall
class C:
    @tracer
    def spam(self, a,b,c): return a+b+c
x=C()
print(x.spam(1,2,3))
print(x.spam('a','b','c'))


class A:
    def act(self): print('A')
class B:
    def act(self): print('B')
class C(A):
    def act(self):
        super().act()
