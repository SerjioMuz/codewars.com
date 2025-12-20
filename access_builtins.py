class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)
    def add (self, other):
        return self.reroute('__add__', other)
    def str (self) :
        return self.reroute('__str__')
    def __getitem__ (self, index):
        return self.reroute('__getitem__', index)
    def __call__ (self, *args, **kargs):
            return self.reroute('__call__', *args, **kargs)