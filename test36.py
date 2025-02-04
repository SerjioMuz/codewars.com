def tower_builder(n):
    return [('.'*(n-i)+('*'*(i*2-1))+'.'*(n-i)) for i in  range(1,n+1)]

    #return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]
    #Метод center() в Python используется для центрирования строки в заданной
    # ширине. Он принимает число символов, в которое нужно центрировать строку.
    # Если строка короче этого числа, она будет расположена по центру, окруженная пробелами.

    #lis=[]
    #lis2=[]
    #for i in range(1,n+1):
    #    lis='.'*(n-i)+('*'*(i*2-1))+'.'*(n-i)
    #    lis2.append(lis)
    #print (lis2)





res = tower_builder(6)
print(res)