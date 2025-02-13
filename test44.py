def count(s):
    #d={}
    #for letter in set(s):
    #    d[letter]=list(s).count(letter)
    #return(d)

    return {letter:s.count(letter) for letter in s}







print(count("aabbccdsdaaaaddzdd"))