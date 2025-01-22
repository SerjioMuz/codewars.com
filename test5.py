def maps(a):
    l=[]
    for i in a:
        l.append(i*2)
    return(l)



res = maps([1,2,3,4,5,6,7,8,9,0])
print(res)

#return [2 * x for x in a]