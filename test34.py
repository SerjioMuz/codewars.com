def row_sum_odd_numbers(n):
    return sum(range((((sum(range(1,n+1)))*2-n*2)+1),(sum(range(1,n+1)))*2,2))

    #f=0
    #s=0
    #for i in range(1,n+1):
    #    f+=i
    #for o in range(((f*2-n*2)+1),f*2,2):
    #    print(o)
    #    s+=o
    #print (s)




res = row_sum_odd_numbers(41)
print(res)