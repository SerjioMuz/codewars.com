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





print(array_rewerse2([1,2,3,4,5,6,'sdsd',7,8,9,0]))
