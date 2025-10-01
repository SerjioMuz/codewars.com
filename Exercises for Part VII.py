"Exercise 1"
def oops():
    return 'spam'[4]
try:
    oops()
except KeyError:
    print ("ERROR")
else:
    print('OK')

