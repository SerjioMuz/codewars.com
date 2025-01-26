def number(stops):
    return sum(map(lambda x: x[0] - x[1], stops))

    #return lambda b: sum(i - o for i, o in b)
    #return sum(i - o for i, o in stops)
    #return sum((i[0]-i[1])for i in bus_stops)







res = number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])
print(res)