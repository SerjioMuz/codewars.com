def binary_array_to_number(arr):
    return int(("".join(map(str,arr))), base=2)
    #return bin('0b'+("".join(map(str,arr))))





print(binary_array_to_number([0,1,1,0]))