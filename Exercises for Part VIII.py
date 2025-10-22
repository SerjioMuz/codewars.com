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

