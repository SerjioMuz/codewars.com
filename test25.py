def high_and_low(numbers):
    return str(max(map(int,(numbers.split(' ')))))+' '+str(min(map(int,(numbers.split(' ')))))
    #return str(f[-1])+' '+str(f[0])








res = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(res)