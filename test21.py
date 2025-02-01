def sum_mix(arr):
    return sum(map(int, arr))
    #return sum(int(i)for i in arr)





res = sum_mix({'5', '0', 9, 3, 2, 1, '9', 6, 7})
print(res)