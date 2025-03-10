def adder(*x):
    s=x[0]
    for i in x[1:]:
        s+=i
    print(s)

adder( )
adder('a','b')
adder([1,2,3],[4,5,6])
adder(1.234, 2.234)
