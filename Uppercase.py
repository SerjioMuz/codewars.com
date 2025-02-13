def uppercase(lowerchar):
    upperchar=[]
    for sumbol in lowerchar:
        upperchar.append(chr(ord(sumbol)-32))
    return ''.join(upperchar)



print(uppercase('klsadjhfasjkgfhssdfkjhjhjhjkdsjkvjskh'))