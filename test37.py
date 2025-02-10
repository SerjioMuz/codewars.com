def find_uniq(arr):
    return min(set(arr), key=arr.count)

     a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]

    a, b = set(arr)
    return a if arr.count(a) == 1 else b



#    if arr[0]==arr[1]:
#        f=arr[0]
#    elif arr[0]==arr[2]:
#        f=arr[0]
#    else:
#        f=arr[1]
#   for i in arr:
#        if i!=f:
 #
  #          return i




res = find_uniq([ 10, 3, 3, 3, 3 ])
print(res)