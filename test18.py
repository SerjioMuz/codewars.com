def count_sheeps(a1, a2):
    return "".join(sorted(set(a1 + a2)))





res = count_sheeps('acb', 'ced')
print(res)
