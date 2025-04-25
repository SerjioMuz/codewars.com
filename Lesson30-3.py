class SkipObject:
    def __init__(self, wrapped):
        self.wrapped=wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped=wrapped
        self.offset=0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

if __name__ == '__main__':
    alpha='abcdef'
    skipper = SkipObject (alpha)
    I=iter(skipper)
    print(next(I), next(I), next(I))
    for x in skipper:
        for y in skipper:
            print(x+y, end=' ')


""" Альтернативная реализация"""
def gen(x):
    for i in range(x): yield i**2

class Squares:
    def __init__(self, start, stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        for value in range(self.start, self.stop+1):
            yield value **2

class Squares:
    def __init__(self, start, stop):
        self.start=start
        self.stop=stop
    def gen(self):
        for value in range(self.start, self.stop+1):
            yield value **2

"""Генератор не основанный на yield"""
class Squares:
    def __init__(self, start, stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)
class SquaresIter:
    def __init__(self, start, stop):
        self.value=start-1
        self.stop=stop
    def __next__(self):
        if self.value==self.stop:
            raise StopIteration
        self.value+=1
        return self.value**2

"""Генератор на основе __iter__ + yield"""
class SkipObject:
    def __init__(self, wrapped):
        self.wrapped=wrapped
    def __iter__(self):
        offset=0
        while offset < len(self.wrapped):
            item=self.wrapped[offset]
            offset+=2
            yield item
