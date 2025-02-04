def get_middle(s):
    return s[len(s)//2-1]+s[len(s)//2] if len(s)%2==0 else s[(len(s) // 2)]
        #print(s[len(s)//2-1]+s[len(s)//2])
    #else:
        #print(s[(len(s) // 2)])



res = get_middle('abcdefjiqkl')
print(res)