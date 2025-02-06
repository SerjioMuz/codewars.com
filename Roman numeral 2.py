number=int(input('Введите число от 1 до 1000-->'))
result=[]
L={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC', 50:'L',40:'XL', 10:'X',9:'IX', 5:'V', 4:'IV',1:'I'}
while number>0:
    for key in L:
        if key <= number:
            number-=key
            result.append(L[key])
print(''.join(result))