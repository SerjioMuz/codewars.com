def is_isogram(string):
    return len(set(string.lower())) == len(string)






res = is_isogram('abCdEfF')
print(res)