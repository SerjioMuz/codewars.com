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

class operators:
    def __getattr__(self, name):
        if name=='age':
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name=='age':
            self.__dict__['_age']=value
        else:
            self.__dict__[name]=value

class AgeDesc(object):
    def __get__(self, instance, owner): return 40
    def __set__(self, instance, value): instance._age=value
class descriptors(object):
    age=AgeDesc()
