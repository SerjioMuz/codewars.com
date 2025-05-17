"Файл listinstanse.py"
class ListInstance:
    def __attrnames(self):
        result=''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instanse of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames())

if __name__=='__main__':
    import textmixing
    textmixing.tester(ListInstance)

"Файл testmixin0.py"
from listinstance import ListInstance
class Super:
    def __init__(self):
        self.data1='spam'
    def ham(self):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2='eggs'
        self.data3=42
    def spam(self):
        pass

if __name__ == "__main__":
    x=Sub()
    print(x)

"Файл testmixin.py"
import importlib
def tester(Listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1='spam'
        def ham(self):
            pass
    class Sub(Super, Listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass
    instanse=Sub()
    print(instanse)
    if sept: print('-' *80)

def testByNames(modname, classname, sept=False):
    modobject=importlib.import_module(modname)
    listerclass=getattr(modobject, classname)
    tester(listerclass,sept)
if __name__=='__main__':
    testByNames('listinstance', 'ListInstance', True)
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree', 'ListTree', False)

"Файл listinherited.py"
class ListInherited:
    def __attrnames(self):
        result=''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:]== '__':
                result +='\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self,attr))
        return result
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' %  (
            self.__class__.__name__,
            id(self),
            self.__attrnames())
if __name__=='__main__':
    import testmixin
    testmixin.tester(ListInherited)

"Файл listinherited2.py"
class ListInherited:
    def __attrnames(self, indent=' '*4):
        result='Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:]== '__':
                unders.append(attr)
            else:
                display=str(getattr(self, attr)) [:82-(len(indent)+len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' %  (
            self.__class__.__name__,
            id(self),
            self.__attrnames())
if __name__=='__main__':
    import testmixin
    testmixin.tester(ListInherited)

"Файл listtree.py"
class ListTree:
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent + 4)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                here, above,
                dots)

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here, above)

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)

"Файл lister.py"
from listinstance import ListInstance
from listinherited import ListInherited
from listtree import ListTree

Lister=ListTree