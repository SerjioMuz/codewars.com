class Wrapper:
    def __init__(self, object):
        self.wrapped=object
    def __getattr__(self, attrname):
        print('Trasse:' + attrname)
        return getattr(self.wrapped, attrname)