def delete_nth(order,max_e):
    #lis=[]
    #for i in order:
    #    if (lis.count(i))<max_e:
    #        lis.append(i)
    #return(lis)


    #lis=[]
    #[lis.append(i) for i in order if lis.count(i)<max_e]
    #return lis


    return [o for i, o in enumerate(order) if order[:i].count(o) < max_e]





res = delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 2)
print(res)