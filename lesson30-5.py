from operator import contains


class Iters:
    def __init__(self, value):
        self.data=value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data

    def __iter__(self):
        print('iter=> next:', end='')
        for x in self.data:
            yield x
            print('next:', end='')

    def __contains__(self, x):
        print('contains:', end='')
        return x in self.data

if __name__=='__main__':
    x=Iters([1,2,3,4,5])
    print(3 in x)
    for i in x:
        print(i, end=' | ')
        print()
        print([i**2 for i in x])
        print(list(map(bin,x)))
        I=iter(x)
        while True:
            try:
                print(next(I), end=' @ ')
            except StopIteration:
                break