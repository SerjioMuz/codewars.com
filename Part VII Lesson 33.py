class AlreadyGotOne(Exception): pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print('got exception')




class Carrer(Exception):
    def __str__(self): return 'So I became a waited...'




def after():
    try:
        fetcher(x,3)
    finally:
        print('after fetcher')
    print('after try')




def kaboom(x,y):
    print(x+y)
try:
    kaboom([1,2,3], 'spam')
except TypeError:
    print('erroorrs')
print('no errors')



class MyError(Exception): pass
def stuff(file):
    raise MyError()
file = open('data', 'w')
try:
    stuff(file)
finally:
    file.close()
print ('not reached')

try:
    raise IndexError('spam')
except IndexError:
    print('propagating')
    raise

try:
    1/0
except Exception as E:
    raise TypeError('Bad') from E

def f(x):
    assert x<0, 'x must be negative'
    return x**2

def reciprocal(x):
    assert x !=0
    return 1/x