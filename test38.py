def tower_builder(n_floors, block_size):
    result=[]; r=1
    for i in range(n_floors):
        for o in range(block_size[1]):
            result.append((('*'*block_size[0])*r).center((n_floors*2*block_size[0])-block_size[0]))
        r+=2
    return (result)


#return [x for s in [[f"{'*'*(x[0]*i*2-x[0]):^{x[0]*n*2-x[0]}}"] * x[1] for i in range(n, 0, -1)] for x in s][::-1]
#tower_builder = lambda n,b:[('*'*(b[0]*(2*c-1))).center(b[0]*(2*n-1)) for c in range(1,n+1) for _ in range(1,b[1]+1)]

print(tower_builder(3,(4,2)))
