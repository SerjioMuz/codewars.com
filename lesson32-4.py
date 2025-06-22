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

"Файл spam_class.py"
class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances=Spam.numInstances+1
    def printNumInstances(self):
        print('Number of instances created: %s' % Spam.numInstances)


"Файл bothmethods.py"
class Methods:
    def imeth(self, x):
        print([self, x])
    def smeth(x):
        print([x])
    def cmeth(cls,x):
        print(cls,x)
    smeth=staticmethod(smeth)
    cmeth=classmethod(cmeth)

"Файл spam_static.py"
class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances +=1
    def printNumInstances():
        print('Number of instances: %s' % Spam.numInstances)
    printNumInstances=staticmethod(printNumInstances)
class Sub(Spam):
    def printNumInstances():
        print('Extra stuff...')
        Spam.printNumInstances()
    printNumInstances=staticmethod(printNumInstances)


class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances +=1
    def printNumInstances(cls):
        print('Number of instances: %s' % cls.numInstances)
    printNumInstances=classmethod(printNumInstances)

