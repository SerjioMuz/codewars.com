def get_grade(s1, s2, s3):
    dic={10:'A',9:'A',8:'B',7:'C',6:'D'}
    n = (s1+s2+s3)//10//3
    if n<6:
        return 'F'
    return (dic[n])

return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
return 'FFFFFFDCBAA'[sum(s)//30]


res = get_grade(50, 50, 50)
print(res)