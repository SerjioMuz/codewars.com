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
        print('ERROR2', x)
    else:
        print('OK')
