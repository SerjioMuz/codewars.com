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
