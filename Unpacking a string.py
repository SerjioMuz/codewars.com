text='a2f4s4e9r3g1'
res=''
symbol=''
for i in text:
    if i.isdigit():
        res=res+(symbol*int(i))
    else:
        symbol=i
print(res)