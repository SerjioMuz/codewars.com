"Exercise 1"
def oops():
    return 'spam'[4]
try:
    oops()
except KeyError:
    print ("ERROR")
else:
    print('OK')

"Exercise 2"
class MyError(Exception): pass
def oops():
    raise MyError('Spam')
def doomed():
    try:
        oops()
    except IndexError:
        print ("ERROR1")
    except MyError as x:
        print('ERROR2',MyError, x)
    else:
        print('OK')

"Exercise 3"
import sys, traceback
def safe(calle, *pargs, **kargs):
    try:
        calle (*pargs, ** kargs)
    except:
        traceback.print_exc()
        print ('Got %s, %s' % (sys.exc_info()[0], sys.exc_info()[1]))
if __name__=='__main__':
    import oops2
    safe(oops2.oops)

import sys, traceback
def safe(calle):
    def callproxy(*pargs, **kargs):
        try:
            return calle(*pargs, **kargs)
        except:
            traceback.print_exc()
            print('Got %s, %s' % (sys.exc_info()[0], sys.exc_info()[1]))
            raise
    return callproxy
if __name__=='__main__':
    import oops2
    @safe
    def test():
        oops2.oops()
    test()
