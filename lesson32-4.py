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

