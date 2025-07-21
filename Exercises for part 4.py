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


"Файл mysub.py"
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

class MyListSub(MyList):
    calls=0
    def __init__(self, start):
        self.adds=0
        MyList.__init__(self, start)
    def __add__(self, other):
        print('add: ' + str(other))
        MyListSub.calls +=1
        self.adds +=1
        return  MyList.__add__(self, other)
    def stats(self):
        return self.calls, self.adds






class Attrs:
    def __getattr__(self, name):
        print('get %s' % name)
    def __setattr__(self, name, value):
        print('set %s %s' % (name, value))


"Файл multiset.py"
from setwrapper import Set
class MultiSet(Set):
    def intersect(self, *others):
        res=[]
        for x in self:
            for other in others:
                if x not in other: break
            else:
                res.append(x)
        return Set(res)
    def union(*args):
        res=[]
        for seg in args:
            for x in seg:
                if not x in res:
                    res.append(x)
        return Set(res)




class ListInstance:
    def __attrnames(self):
        result=''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instanse of %s(%s), address %s:\n%s>' % (
            self.__class__.__name__,
            self.__supers(),
            id(self),
            self.__attrnames())
    def __supers(self):
        names=[]
        for super in self.__class__.__bases__:
            names.append(super.__name__)
        return', '.join(names)

if __name__=='__main__':
    import testmixin
    testmixin.tester(ListInstance)





class Lunch:
    def __init__(self):
        self.cust=Customer()
        self.empl=Employee()
    def order(self, foodName):
        self.cust.placeOrder(foodName, self.empl)
    def result(self):
        self.cust.printFood()

class Customer:
    def __init__(self):
        self.food=None
    def placeOrder(self, foodName, employee):
        self.food=employee.takeOrder(foodName)
    def printFood(self):
        print(self.food.name)


class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)

class Food:
    def __init__(self, name):
        self.name=name

if __name__=='__main__':
    x=Lunch()
    x.order('spam')
    x.result()


class Animal:
    def speak(self): print('AnimalXXX')
    def reply(self):
        self.speak()
    def www(self): print('rrrrrrrrrrrrrrrrrrrrrrrrrr')

class Mammal(Animal):
    def speak(self): print('MammalXXX')

class Cat(Mammal):
    def speak(self): print('CatXXX')

class Dog(Mammal):
    def speak(self): print('DogXXX')

class Primate(Mammal):
    def speak(self): print('PrimateXXX')

class Hacker(Primate): pass

