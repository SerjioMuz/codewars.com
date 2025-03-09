import timeit
#print(min(timeit.repeat(stmt="[x**2 for x in range(100000)]", number=100, repeat=5)))
#print(min(timeit.repeat(number=100000, repeat=10, stmt='L=[1,2,3,4,5]\nfor i in range(len(L)):L[i]+=1')))
print(min(timeit.repeat(number=100000, repeat=10, stmt='L=[1,2,3,4,5]\nM=[x+1 for x in L]')))
