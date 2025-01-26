def count_sheeps(sheep):
    sheeps=0
    for i in sheep:
        try:
            sheeps=sheeps+i
        except:
            sheeps=sheeps
    print(sheeps)





    #print (len(sheep))
    #for i in sheep:
    #   print(i)






res = count_sheeps([True,  'ffff',  True,  False, True,  True,  True])
print(res)
