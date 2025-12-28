class MetaOne(type):
    def __new__ (meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Eggs: pass

print('making class')

class Spam(Eggs, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


#___________________________________________________________________________
class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    def __init__ (Class, classname, supers, classdict) :
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs: pass

print('making class')

class Spam(Eggs, metaclass=MetaTwo):
    data = 1
    def meth (self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))



#______________________________________________________________________________
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)

class Eggs: pass

print('making class')

class Spam(Eggs, metaclass=MetaFunc):
    data =1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))



#______________________________________________________________________________
class MetaObj:
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__diet__.keys()))

class Eggs: pass

print('making class')

class Spam(Eggs, metaclass=MetaObj()):
    data = 1

    def meth(self, arg):
        return self.data + arg
        print('making instance')

X = Spam()
print('data:', X.data, X.meth(2))



#______________________________________________________________________________
class SuperMeta(type):
    def __call__ (meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__ (meta, classname, supers, classdict)
    def __init__ (Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__ .keys ()))

print('making metaclass')

class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__ .keys ()))

class Eggs: pass

print('making class')

class Spam(Eggs, metaclass=SubMeta):
    data = 1
    def meth(self, arg) :
        return self.data + arg

print('making instance')

X = Spam()

print('data:', X.data, X.meth(2))


#______________________________________________________________________________
