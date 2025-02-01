def count_positives_sum_negatives(arr):
    if not arr: return arr
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]

return [len([i for i in arr if i > 0]),sum([i for i in arr if i < 0])] if arr else []











res = count_positives_sum_negatives([0])
print(res)