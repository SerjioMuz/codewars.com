def remove_smallest(numbers):
    numbers2 = list(numbers)
    if numbers:
        numbers2=list(numbers)
        numbers2.remove(min(numbers2))
    return numbers2



print(remove_smallest([]))