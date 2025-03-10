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






print(copyDict(z='q', x='w',c='e', v='r'))