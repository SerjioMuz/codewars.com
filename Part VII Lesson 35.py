"Файл classexc.py"
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass
def raiser0():
    x=General()
    raise x
def raiser1():
    x=Specific1()
    raise x
def raiser2():
    x=Specific2()
    raise x
for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        import sys
        print('caught: %s' % sys.exc_info()[0])

"Файл classexc2.py"
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass
def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()
for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as x:
        print('caught: %s' % x.__class__)

