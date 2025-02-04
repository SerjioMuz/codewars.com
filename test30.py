def is_pangram(st):
    f='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    return all(map(lambda x: x in (str(st).lower()), f))
#return set(string.ascii_lowercase).issubset(s.lower())
#return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False
#return set(s.lower()) >= set(string.ascii_lowercase)
#return all(l in s.lower() for l in ascii_lowercase)
#return all(i in s.lower() for i in f)


res = is_pangram([ "qwertyuiop[]';lkjhgfdsaxcvbnm,",".qwertyuiop[]';lkjhgfdsaxcvbnmz,."])
print(res)