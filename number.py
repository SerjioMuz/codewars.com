class Number:
    def __init__(self, start):
        self.data=start
    def __sub__(self, other):
        return Number(self.data-other)

class Indexer:
    data=[5,6,7,8,9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

class C:
    def __index__(self):
        return 255

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

