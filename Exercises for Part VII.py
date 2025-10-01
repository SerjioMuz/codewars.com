"Exercise 1"
def oops():
    return 'spam'[4]
try:
    oops()
except IndexError:
    print ("ERROR")
else:
    print('OK')

