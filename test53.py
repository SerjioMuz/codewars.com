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


print(addDict({4:'d',5:'e',6:'f'}, {1:'a',2:'b',3:'c'}))
print(addDict([1,2,3],[4,5,6]))
















