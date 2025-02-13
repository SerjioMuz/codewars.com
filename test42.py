def longest_consec(strarr, k):
    sorting=''
    d=k
    if strarr and 0<k<=len(strarr):
        while d<=len(strarr):
            s=''.join(strarr[(d-k):(d)])
            d+=1
            if len(s)>len(sorting):
                sorting=s
        return sorting
    else:
        return("")



def longest_consec(strarr, k):
    length = len(strarr)
    if not length or k > length or k <= 0:
        return ""
    else:
        lst = [''.join(strarr[i:i+k]) for i in range(length)]
        return max(lst, key=len)

#return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
#return max(("".join(strarr[i:i+k]) for i in range(len(strarr)-k+1)), key=lambda x: len(x)) if strarr and k > 0 and k <= len(strarr) else ""


print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"],3))