lowerchar='abcdefghijklmnopqrstuvwxyz'
upperchar=[]
for sumbol in lowerchar:
    upperchar.append(chr(ord(sumbol)-32))
print (''.join(upperchar))