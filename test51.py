def max_sequence(arr):
    maxs=0
    j=0
    if arr and 0 < max(arr):
        for i in range(1,len(arr)+1):
            ti=sum(arr[j:i])
            if 0<=ti:
                if maxs<ti:
                    maxs=ti
            else:
                j=i
    return maxs






print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))