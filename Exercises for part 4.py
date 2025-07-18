"Файл adder.py"
class Adder:
    def add(self, x,y):
        print('Not Implement')
    def __init__(self, start=[]):
        self.data=start
    def __add__(self, other):
        return self.add(self.data, other)

class ListAdder(Adder):
    def add(self, x,y):
        return x+y

class DictAdder(Adder):
    def add(self, x,y):
        new={}
        for k in x.keys(): new[k] = x[k]
        for k in y.keys(): new[k] = y[k]
        return new

"Файл adder2.py"
class Adder:
    def __init__(self, start=[]):
        self.data=start
    def __add__(self, other):
        return self.add(other)
    def add(self,y):
        print('Not Implement')

class ListAdder(Adder):
    def add(self,y):
        return self.data+y

class DictAdder(Adder):
    def add(self,y):
        d=self.data.copy()
        d.update(y)
        return d


"Файл mylist.py"
class MyList:
    def __init__(self, start):
        self.wrapped=list(start)
    def __add__(self, other):
        return MyList(self.wrapped+other)
    def __mul__(self, time):
        return MyList(self.wrapped*time)
    def __getitem__(self, offset):
        return self.wrapped[offset]
    def __len__(self):
        return len(self.wrapped)
    def append(self, node):
        self.wrapped.append(node)
    def __getattr__(self, name):
        return getattr(self.wrapped, name)
    def __repr__(self):
        return repr(self.wrapped)
if __name__=='__main__':
    x=MyList('spam')
    print(x)
    print(x[2])
    print(x[1:])
    print(x+['eggs'])
    print(x*3)
    x.append('a')
    x.sort()
    print(' '.join(c for c in x))
