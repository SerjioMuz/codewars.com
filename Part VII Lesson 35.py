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

class FormatError(Exception):
    def __init__(self, line, file):
        self.line=line
        self.file=file

def parser():
    raise FormatError(42, file='spam.txt')

try:
    parser()
except FormatError as X:
    print('Error at: %s %s' % (X.file, X.line))


"Файл excparse.py"
from __future__ import print_function
class FormatError(Exception):
    logfile='formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log=open(self.logfile, 'a')
        print('Error at:', self.file, self.line, file=log)
def parser():
    raise FormatError(40, 'spam.txt')
if __name__=='__main__':
    try:
        parser()
    except FormatError as exc:
        exc.logerror()

"Файл nestexc.py"
def action2():
    print(1+[])
def action1():
    try:
        action2()
    except TypeError:
        print('inner try')

try:
    action1()
except TypeError:
    print('outer try')

try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')



class ExitLoop(Exception): pass
try:
    while True:
        while True:
            for i in range (10):
                if i > 3: raise ExitLoop
                print('loop3: %s' % i)
            print('loop2')
        print('loop')
except ExitLoop:
    print('continuing')


"Файл exiter.py"
import sys
def bye():
    sys.exit(40)
try:
    bye()
except Exception:
    print('got it')
print('continuing')

mydictionary={}
print('OK1')
try:
    x=mydictttttionary['spam']
except KeyError:
    x=None
    print('OK2')
print('OK3')