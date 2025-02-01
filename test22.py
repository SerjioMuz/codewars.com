def to_jaden_case(string):
    lis=(string.lower()).split(' ')
    for i in range(len(lis)):
        lis[i]=lis[i][0].upper()+lis[i][1:]
    return ' '.join(lis)






res = to_jaden_case("HoW caN mirrors be real if our eyes aren't real")
print(res)