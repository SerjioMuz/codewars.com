text='aaffffsssseeeeeeeeerrrghhhhhh'
symbol=''
count=0
res=''
for i in text:
    if symbol == i:
        count += 1
    else:
        if count!=0:
            res=res+symbol+str(count)
        symbol = i
        count = 1
print(res)