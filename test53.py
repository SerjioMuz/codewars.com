import math


def adder(**args):
    l=list(args.values())
    sum=l[0]
    for i in l[1:]:
        sum+=i
    print(sum)

#adder(z='q', x='w',c='e', v='r')

def copyDict(**dict):
    d=dict
    dict2={}
    for i in list(d.keys()):
        dict2.update({i:dict[i]})

    return dict2
#print(copyDict(z='q', x='w',c='e', v='r'))

def addDict (dict1, dict2):
    if type(dict1)==list and type(dict2)==list:
        return dict1+dict2
    else:
        dict3={}
        for i in list(dict1.keys()):
            dict3.update({i:dict1[i]})
        for j in list(dict2.keys()):
            dict3.update({j:dict2[j]})
        return dict3


#print(addDict({4:'d',5:'e',6:'f'}, {1:'a',2:'b',3:'c'}))
#print(addDict([1,2,3],[4,5,6]))


def f4(a,*b,**c): print(a,b,c)
#f4(1,2,3, x=2, y=3)

def f5(a,b=2,c=3): print(a,b,c)
#f5(1,4)

def f6(a,b=2,*c): print(a,b,c)
#f6(1,3,4)

def prime(y):
    x=y//2
    while x>1:
        if y%x==0:
            print(y, 'has factor', x)
            break
        x-=1
    else:
        print(y, 'is prime')

#prime(0)

#L=[2,4,9,16,25]
#L2=[]
#for i in L:
#    L2.append(math.sqrt(i))
#print(L2)

#print(list(map(lambda x: math.sqrt(x),[2,4,9,16,25])))
#print([math.sqrt(x) for x in [2,4,9,16,25]])
#gen=list(math.sqrt(x) for x in [2,4,9,16,25])
#print(gen)

import sys

sys.setrecursionlimit(3000)

def countdown(x):
    if x >0:
        print(x)
        countdown(x-1)

#countdown(5)

def fact1(n):
    if n ==1:
        return 1
    return fact1(n - 1) * n
print(fact1(1000))

def fact2(n):
    from functools import reduce
    return reduce((lambda x,y:x*y), list(range(1,n+1)))
print(fact2(1000))

def fact3(n):
    sum=1
    for  i in range(1,n+1):
        sum*=i
    return sum
print(fact3(1000))

def fact4(n):
    import math
    return math.factorial(n)

#print(fact4(1000))

import math
import timeit
print(min(timeit.repeat(number=1000, repeat=5, stmt=
"""def fact3(n):
    sum=1
    for  i in range(1,n+1):
        sum*=i
    return sum
fact3(1000)""")))

import timeit
print(min(timeit.repeat(number=1000, repeat=5, stmt=
"""def fact2(n):
    from functools import reduce
    return reduce((lambda x,y:x*y), list(range(1,n+1)))
fact2(1000)""")))

import timeit
print(min(timeit.repeat(number=1000, repeat=5, stmt=
"""def fact1(n):
    if n ==1:
        return 1
    return fact1(n - 1) * n
fact1(1000)""")))

import timeit
print(min(timeit.repeat(number=1000, repeat=5, stmt=
"""def fact3(n):
    return n*i for i in range(1,n+1)
fact3(1000)""")))

def fact3(n):
    return [n*i for i in range(n, 1, -1)]
print(fact3(5))