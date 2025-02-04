def unique_in_order(sequence):
    rest=[]
    if sequence:
        for i in range(len(sequence)-1):
            if (i+1) <= len(sequence):
                if sequence[i]!=sequence[i+1]:
                    rest.append(sequence[i])
        rest.append(sequence[(len(sequence)-1)])
        return rest
    else:
        return []

    #return [ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1]]

    #return [sequence[i-1] for i in range(1, len(sequence)+1) if sequence[(i)] !=sequence[abs(i-1)]]
    #return [o for i, o in enumerate(sequence,1) if sequence[(len(sequence)-i)*-1] !=o]
    #return[o for i, o in enumerate(sequence) if sequence[:i].count(o) < max_e]


res = unique_in_order('')
print(res)