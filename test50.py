def max_sequence(arr):
    m=[]
    for num in range(2, len(arr)+1):
        for n in range(len(arr)):
            m.append(sum(arr[n:n+num]))
                #m=sum(arr[n:n+num])
    return max(m)









print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))