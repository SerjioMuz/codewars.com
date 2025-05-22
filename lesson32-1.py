"Файл setwrapper.py"
class Set:
    def __init__(self, value=[]):
        self.data=[]
        self.concat(value)
    def intersect(self, other):
        res=[]
        for  x in self.data:
            if x in other:
                res.append(x)
        return Set(res)
    def union(self, other):
        res=self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)
    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

def __len__(self): return len(self.data)
def __getitem__(self, key): return self.data[key]
def __and__(self, other): return self.intersect(other)
def __or__(self, other): return self.union(other)
def __repr__(self): return "Set:" + repr(self.data)
def __item__(self): return iter(self.data)


"Файл tupesub-class.py"
class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset-1)
if __name__=='__main__':
    print(list('abc'))
    x=MyList('abc')
    print(x)
    print(x[1])
    print(x[3])
    x.append('spam'); print(x)
    x.reverse(); print(x)
