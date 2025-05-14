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