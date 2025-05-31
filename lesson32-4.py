class operators:
    def __getattr__(self, name):
        if name=='age':
            return 40
        else:
            raise AttributeError(name)

class properties(object):
    def getage(self):
        return 40
    age=property(getage, None, None, None)
