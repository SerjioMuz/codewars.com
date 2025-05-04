class Truth:
    def __bool__(self): return True

class Truth:
    def __bool__(self): return False

class Truth:
    def __len__(self): return 0

class Truth:
    def __bool__(self): return True
    def __len__(self): return 0

class Life:
    def __init__(self, name='unknown'):
        print('Hello'+ name)
        self.name=name
    def live(self):
        print(self.name)
    def __del__(self):
        print('Goodbye' + self.name)

