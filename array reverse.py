def array_rewerse(lis):
    lisRevers=[]
    for index in range(len(lis)-1, -1, -1):
        lisRevers.append(lis[index])
    return lisRevers


def array_rewerse2(lis):
    for index in range(0, len(lis)):
        lis.insert(index,lis[-1])
        del lis[-1]
    return lis


def array_rewerse3(lis):
    lisRevers=[]
    for index in range(len(lis)-1, -1, -2):
        lisRevers.append(lis[index])
        if index>0:
            lisRevers.append(lis[index-1])
    return lisRevers


def array_rewerse4(lis):
    for index in range(0, len(lis),2):
        lis.insert(index,lis[-1])
        del lis[-1]
        lis.insert(index+1, lis[-1])
        del lis[-1]
    return lis


print(array_rewerse4([1,2,3,4,5,'j',6,7,8,9,0]))
