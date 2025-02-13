def solution(s):
    #lis=[]
    #for letter in s:
    #    if letter.isupper():
    #        lis.append(' '+letter)
    #    else:
    #        lis.append(letter)
    #return ''.join(lis)
    return ''.join(' '+letter if letter.isupper() else letter for letter in s
    return ' '.join([x for x in re.findall('.[^A-Z]*', s)])
return re.sub(r'([A-Z])', r' \1', s)










print(solution("breakCamelCase"))