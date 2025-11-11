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




