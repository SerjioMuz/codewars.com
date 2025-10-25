"Файл patternparse.py"
import re
text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)


"Файл domparse.py"
from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)

"Файл saxparse.py"
import xml.sax.handler
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__ (self) :
        self.inTitle = False
    def startElement(self, name, attributes):
        if name == ' title':
            self.inTitle = True
    def characters(self, data):
        if self.inTitle:
            print(data)
    def endElement(self, name):
        if name == 'title' :
            self.inTitle = False
import xml.sax
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')

"Файл etreeparse.py"
from xml.etree.ElementTree import parse
tree = parse('mybooks.xml')
for E in tree.findall('title'):
    print(E.text)


import sys
f = open('py33-windows-launcher.html', encoding='utf8')
t = f.read()
for (i, c) in enumerate (t) :
    try:
        x = c.encode(encoding= 'ascii')
    except:
        print(i, sys.exc_infо()[0])

class Person:
    def __init__ (self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self) :
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")


class PropSquare:
    def __init__ (self, start):
        self.value = start
    def getX(self):
        return self.value ** 2
    def setX(self, value):
        self.value = value
    X = property(getX, setX)


class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')
class Subject:
    attr=Descriptor()

class Name:
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__ (self, instance, value):
        print('change. . .')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:
    def __init__ (self, name):
        self._name = name
    name = Name ()


class Person:
    def __init__ (self, name):
        self._name = name
    name = Name()
    class Name:
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change. . .')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name



class DescSquare:
    def __init__(self, start):
        self.value=start
    def __get__(self, instance, owner):
        return self.value**2
    def __set__(self, instance, value):
        self.value=value

class Client1:
    x=DescSquare(3)

class Client2:
    x=DescSquare(32)


class DescState:
    def __init__(self, value):
        self.value=value
    def __get__(self, instance, owner):
        print('DescState get')
        return self.value*10
    def __set__(self, instance, value):
        print('DescState set')
        self.value=value

class CalcAttrs:
    x=DescState(2)
    y=3
    def __init__(self):
        self.z=4



class InstState:
    def __get__(self, instance, owner):
        print ('InstState get')
        return instance._X*10
    def __set__ (self, instance, value):
        print('InstState set')
        instance._X = value

class CalcAttrs:
    X = InstState ()
    Y = 3
    def __init__ (self) :
        self._X = 2
        self.Z = 4



class DescBoth:
    def __init__(self, data):
        self .data = data
    def __get__ (self, instance, owner):
        print('get')
        return '%s, %s' % (self.data, instance.data)
    def __set__(self, instance, value):
        print('set')
        instance.data = value

class Client:
    def __init__ (self, data) :
        self.data = data
    managed = DescBoth('spam')



class Property:
    def __init__ (self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
    def __get__ (self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError ("can't get attribute")
        return self.fget(instance)
    def __set__ (self, instance, value):
        if self.fset is None:
            raise AttributeError ("can't set attribute")
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError ("can* t delete attribute")
        self.fdel(instance)

class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)

class Catcher():
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))


class Wrapper:
    def __init__(self, object):
        self.wrapper=object
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapper, attrname)


class Person:
    def __init__ (self, name):
        self._name = name
    def __getattr__ (self, attr):
        print('get:' ,attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)
    def __setattr__ (self, attr, value):
        print ('set:' ,attr)
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value
    def __delattr__(self, attr):
        print('del:' ,attr)
        if attr == 'name' :
            attr = '_name'
            del self.__dict__ [attr]


class Person:
    def __init__ (self, name):
        self._name = name
    def __getattribute__ (self, attr):
        print('get:' , attr)
        if attr == 'name':
            attr = '_name'
        return object.__getattribute__(self, attr)

    def __setattr__ (self, attr, value):
        print ('set:' ,attr)
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value
    def __delattr__(self, attr):
        print('del:' ,attr)
        if attr == 'name' :
            attr = '_name'
            del self.__dict__ [attr]


class AttrSquare:
    def __init__ (self, start):
        self.value = start
    def __getattr__ (self, attr):
        if attr == 'X':
            return self.value ** 2
        else:
            raise AttributeError(attr)
    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value




class AttrSquare:
    def __init__ (self, start):
        self.value = start
    def __getattribute__ (self, attr):
        print('get')
        if attr == 'X':
            return self.value ** 2
        else:
            return object.__getattribute__(self, attr)
    def __setattr__(self, attr, value):
        print('set')
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)


class AttrSquare:
    def __init__ (self, start):
        self.value = start
    def __getattribute__ (self, attr):
        print('get')
        if attr == 'X':
            return object.__getattribute__(self,'value') ** 2
        else:
            return object.__getattribute__(self, attr)
    def __setattr__(self, attr, value):
        print('set')
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)



class GetAttr:
    attr1=1
    def __init__(self):
        self.attr2=2
    def __getattr__(self, attr):
        print('Get:' +attr)
        if attr=='attr3':
            return 3
        else:
            raise AttributeError(attr)

X=GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-'*20)

class GetAttr:
    attr1=1
    def __init__(self):
        self.attr2=2
    def __getattribute__(self, attr):
        print('Get:' +attr)
        if attr=='attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X=GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-'*20)



class Powers:
    def __init__ (self, square, cube):
        self._square = square
        self._cube = cube
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)
    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

X=Powers(3,4)
print(X.square)
print(X.cube)
X.square=5
print(X.square)

class DescSquare(object):
    def __get__ (self, instance, owner):
        return instance._square ** 2
    def __set__ (self, instance, value):
        instance._square = value

class DescCube(object):
    def __get__ (self, instance, owner):
        return instance._cube ** 3

class Powers(object):
    square = DescSquare ()
    cube = DescCube ()
    def __init__ (self, square, cube):
        self._square = square
        self._cube = cube

X=Powers(3,4)
print(X.square)
print(X.cube)
X.square=5
print(X.square)

class Powers:
    def __init__ (self, square, cube):
        self._square = square
        self. _cube = cube
    def __getattr__ (self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)
    def __setattr__ (self, name, value):
        if name == 'square':
            self.__dict__ ['_square'] = value
        else:
            self.__dict__[name] = value

X=Powers(3,4)
print(X.square)
print(X.cube)
X.square=5
print(X.square)


class Powers:
    def __init__ (self, square, cube):
        self._square = square
        self. _cube = cube
    def __getattribute__ (self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self,name)
    def __setattr__ (self, name, value):
        if name == 'square':
            object.__setattr__(self,'_square', value)
        else:
            object.__setattr__(self, name, value)

X=Powers(3,4)
print(X.square)
print(X.cube)
X.square=5
print(X.square)

class GetAttr:
    eggs = 88
    def __init__ (self) :
        self.spam = 77
    def __len__ (self):
        print('__len__ : 42')
        return 42
    def __getattr__ (self, attr) :
        print ('getattr: ' + attr)
        if attr == '__str__ ':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:
    eggs = 88
    def __init__ (self):
        self.spam = 77
    def __len__ (self):
        print ('__len__ : 42')
        return 42
    def __getattribute__(self, attr):
        print ('getattribute: ' + attr)
        if attr == '__str__ ':
            return lambda *args: ' [GetAttribute str]'
        else:
            return lambda *args: None

#for Class in GetAttr, GetAttribute:
#    print('\n' + Class.__name__.ljust(50, '='))
X = GetAttribute()
X.eggs
X.spam
X.other
len(X)
try: X[0]
except: print('fail []')


class Person:
    def __init__ (self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split () [-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__ (self):
        return ' [Person: %s, %s] ' % (self.name, self.pay)

class Manager:
    def __init__ (self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise (percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
#    def __repr__ (self):
#        return str(self.person)

if __name__ == '__main__' :
    sue = Person('Sue Jones', job='dev(', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    print(tom.lastName())
    tom.giveRaise(.10)
    print (tom)


