def correct(s):
    res=[]
    dict={'5':"S", '0':"O", '1':"I"}
    for i in s:
        res.append((dict.get(i,i)))
    return ''.join(res)

#return ''.join({'0':'O', '5':'S', '1':'I'}.get(c, c) for c in string)
#return s.replace("5", "S").replace("0", "O").replace("1", "I")
#return string.translate(str.maketrans("501", "SOI"))



print(correct("51NGAP0RE"))