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
