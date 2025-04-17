class MixedNames:
    data='spam'
    def __init__(self, value):
        self.data=value
    def display(self):
        print(self.data, MixedNames.data)


class NextClass:
    def printer(self, text):
        self.message=text
        print(self.message)


"""class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):
        print('standart Sub.method')
        Super.method(self)
        print('ending Sub.method')"""


class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError ('action must be defined')


class Sub(Super):
    def action(self): print('spam')