from curses import wrapper


def d1(F): return(F)
def d2(F): return(F)
def d3(F): return(F)

@d1
@d2
@d3
def func():
    print('spam')
func()


def d1(F):
    print(1)
    return lambda: 'x' + F()
def d2(F):
    print(2)
    return lambda: 'y' + F()
def d3(F):
    print(3)
    return lambda: 'z' + F()

@d1
@d2
@d3
def func():
    print(4)
    return 'spam'
print(func())

"Файл decorator1.py"
class tracer:
    def __init__(self, func):
        self.calls=0
        self.func=func
    def __call__(self, *args):
        self.calls +=1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)
@tracer
def spam(a,b,c):
    print(a+b+c)

@tracer
def spam1(a,b):
    print(a+b)

@tracer
def spam2(a):
    print(a)




calls=0
def tracer(func, *args):
    global calls
    calls += 1
    print ('call %s to %s' % (calls, func.__name__))
    func(*args)
def spam(a, b, c):
    print(a, b, c)
def spam1(a, b, c):
    print(a, b, c)


class tracer:
    def __init__ (self, func):
        self.calls = 0
        self. func = func
    def __call__ (self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__ ))
        return self.func(*args,**kwargs)

@tracer
def spam(a, b, c) :
    print (a + b + c)

@tracer
def eggs(x,y):
    print(x ** y)



calls=0
def tracer(func):
    def wrapper(*args, **kwargs):
        global calls
        calls+=1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper
@tracer
def spam(a, b, c) :
    print (a + b + c)

@tracer
def eggs(x,y):
    print(x ** y)



def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls+=1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper
@tracer
def spam(a, b, c) :
    print (a + b + c)

@tracer
def eggs(x,y):
    print(x ** y)



def tracer(func):

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls=0
    return wrapper
@tracer
def spam(a, b, c) :
    print (a + b + c)

@tracer
def eggs(x,y):
    print(x ** y)



class tracer:
    def __init__ (self, func):
        self .calls = 0
        self. func = func
    def __call__ (self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
@tracer
def spam(a, b, с) :
    print(a + b + с)



class Person:
    def __init__(self, name, pay):
        self.name= name
        self.pay= pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (0.1+percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]



def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls+=1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

@tracer
def spam(a,b,c):
    print(a,b,c)

@tracer
def eggs(N):
    return 2**N

spam(1,2,3)
spam(a=4, b=5, c=6)
print(eggs(32))






class tracer:
    def __init__ (self, func):
        self .calls = 0
        self. func = func
    def __call__ (self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        return wrapper(self,instance)

class wrapper:
    def __init__(self, desc, subj):
        self.desc=desc
        self.subj=subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)

@tracer
def spam(a,b,c):
    print(a,b,c)

class Person:
    def __init__(self, name, pay):
        self.name= name
        self.pay= pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0+percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]




lass tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper

@tracer
def spam(a, b, c):
    print(a, b, c)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]



spam(1,2,3)
spam(a=4, b=5, c=6)


print('methods')
bob=Person('Bob Smith', 50000)
sue=Person('Sue Jonson', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(int(sue.pay))
print(bob.lastName(), sue.lastName())




"Файл timerdeco1.py"
import time
class timer:
    def __init__(self, func):
        self.func=func
        self.alltime=0
    def __call__(self, *args, **kwargs):
        start=time.perf_counter()
        result=self.func(*args, **kwargs)
        elapsed=time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x*2 for x in range(N)]

@timer
def mapcall(N):
    return list(map((lambda x: x*2), range(N)))

result=listcomp(5)

listcomp(50000)
listcomp(50000)
listcomp(1000000)
print(result)
print(listcomp.alltime)
print("")
result=mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print(mapcall.alltime)


"файл timerdeco2.py"
import  time
def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.perf_counter()
            result = self.func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                format='%s %s: %.5f, %.5f'
                values=(label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer





import sys
from timerdeco2 import timer
@timer(trace=True, label='[CCC]==>')
def listcomp(N):
    return [x*2 for x in range(N)]

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x*2), range(N)))

for func in (listcomp, mapcall):
    result=func(5)
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime=%s\n' % func.alltime)
print('**map/comp= %s' % round(mapcall.alltime / listcomp.alltime, 3))


"файл singletons.py"
instances = {}
def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__ (self, val):
        self.attr = val

bob = Person('Bob', 40, 10)
print (bob.name, bob.pay())
sue = Person('Sue', 50, 20)
print (sue.name, sue.pay())
X = Spam(val=42)
Y = Spam(99)
print(X.attr, Y.attr)



def singleton(aClass):
    instance = None
    def onCall(*args, **kwargs):
        nonlocal instance
        if instance == None:
            instance = aClass(*args, **kwargs)
        return instance
    return onCall

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__ (self, val):
        self.attr = val

bob = Person('Bob', 40, 10)
print (bob.name, bob.pay())
sue = Person('Sue', 50, 20)
print (sue.name, sue.pay())
X = Spam(val=42)
Y = Spam(99)
print(X.attr, Y.attr)










class singleton:
    def __init__ (self, aClass) :
        self.aClass = aClass
        self.instance =None
    def __call__ (self, *args, **kwargs) :
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__ (self, val):
        self.attr = val

bob = Person('Bob', 40, 10)
print (bob.name, bob.pay())
sue = Person('Sue', 50, 20)
print (sue.name, sue.pay())
X = Spam(val=42)
Y = Spam(99)
print(X.attr, Y.attr)



class Wrapper:
    def __init__ (self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)




"файл interfacertacer.py"
def Tracer (aClass):
    class Wrapper:
        def __init__ (self, *args, **kargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)
        def __getattr__ (self, attrname):
            print ('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper

#if __name__ == '__main__' :
@Tracer
class Spam:
    def display (self):
        print('Spam! ' * 8)

@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate




class Tracer:
    def __init__ (self, aClass):
        self.aClass = aClass
    def __call__ (self, *args):
        self.wrapped = self.aClass(*args)
        return self
    def __getattr__ (self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)

@Tracer
class Person:
    def __init__ (self, name):
        self.name = name




registry = {}
def register(obj):
    registry [obj .__name__ ] = obj
    return obj

@register
def spam(x):
    return(x**2)

@register
def ham(x):
    return(x ** 3)
@register
class Eggs:
    def __init__ (self, x):
        self.data = x ** 4
    def __str__ (self) :
        return str(self.data)



"Файл access1.py"
traceMe = False
def trace(*args):
    if traceMe: print ('[' + ''.join(map(str, args)) + ']')
def Private(*privates) :
    def onDecorator(aClass):
        class onlnstance:
            def __init__ (self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__ (self, attr):
                trace('get:' , attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__ (self, attr, value):
                trace ('set:', attr, value)
                if attr == 'wrapped' :
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr (self .wrapped, attr, value)
        return onlnstance
    return onDecorator
if __name__ == '__main__':
    traceMe = True
    @Private('data', 'size')
    class Doubler:
        def __init__ (self, label, start):
            self.label = label
            self.data= start
        def size (self):
            return len (self.data)
        def double (self) :
            for i in range(self.size()) :
                self.data[i] = self.data[i] * 2
        def display(self) :
            print('%s => %s' % (self.label, self.data))

    X = Doubler ('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])


    print(X.label)
    X. display(); X.double(); X.display()
    print(Y.label)
    Y. display(); Y.double()
    Y.label = 'Spam'
    Y.display()

    print(X.size())
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size ())



traceMe = False
def trace(*args):
    if traceMe: print ('[' + ''.join(map(str, args)) + ']')
def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__ (self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__ (self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator
def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))
def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

@Private('age')
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

X=Person('Bob', 40)
X.name
X.name='Sue'
X.name