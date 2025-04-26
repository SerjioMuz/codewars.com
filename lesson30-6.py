class Empty:
    def __getattr__(self, attrname):
        if attrname=='age':
            return 40
        else:
            raise AttributeError(attrname)

class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr=='age':
            self.__dict__[attr]=value+10  "через __dict__" ' object.__setattr__(self, attr, value+10)' "через суперкласс"
        else:
            raise AttributeError(attr+'not allowed')
