number=input('Введите число от 1 до 999-->')
res=[]
k=[0, 100, 10,1][len(number)]
l={1:'I', 2:'II', 3:'III', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
for i,o in enumerate(number,1):
    dig=int(o+('0'*(len(number)-i)))  #Разбиваем число на сотни, десятки и еденицы
    if dig<=(300/k):
        res.append(l[(100/k)]*int(dig/(100/k)))
    elif (900/k)<=dig:
        res.append(l[(100/k)]*int(((1000/k)-dig)/(100/k))+l[(1000/k)])
    elif dig<=(500/k):
        res.append(l[(100/k)]*int(((500/k)-dig)/(100/k))+l[(500/k)])
    elif (500/k)<dig:
        res.append(l[(500/k)]+(l[(100/k)]*int((dig-(500/k))/(100/k))))
    k=k*10   #Счетчик коэффициента для смены расчета сотен,десятков, едениц.
print (''.join(res))
