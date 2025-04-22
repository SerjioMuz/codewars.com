class Number:
    def __init__(self, start):
        self.data=start
    def __sub__(self, other):
        return Number(self.data-other)

class Indexer:
    def __getitem__(self, index):
        return index**2

