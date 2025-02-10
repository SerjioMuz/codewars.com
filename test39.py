def order(sentence):
    #return ' '.join((sentence.split())[(for o in range(1,len([(for i in sentence if i.isdigit())])+1).index(o))])

    #digits=[]
    #res=[]
    #for i in sentence:
    #    if i.isdigit():
    #        digits.append(int(i))
    #for o in range(1,len(digits)+1):
    #    res.append((sentence.split())[digits.index(o)])
    #return ' '.join(res)

    return " ".join(sorted(sentence.split(), key=min))
    #return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))








print(order("4of Fo1r pe6ople g3ood th5e the2"))