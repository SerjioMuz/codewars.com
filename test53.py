def adder(**args):
    l=list(args.values())
    sum=l[0]
    for i in l[1:]:
        sum+=i
    print(sum)

adder(z='q', x='w',c='e', v='r')
