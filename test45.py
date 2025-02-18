from operator import index


def dig_pow(n, p):
    #sum=0
    #for index, val in enumerate((str(n)),0):
    #    sum+=(int(val))**(p+index)
    #if sum%n==0:
    #    return int(sum/n)
    #else:
    #    return -1
    return (sum([(int(val))**(p+index) for index,val in enumerate((str(n)),0)]))/n if (sum([(int(val))**(p+index) for index,val in enumerate((str(n)),0)]))%n==0 else -1





print(dig_pow(46288, 3))