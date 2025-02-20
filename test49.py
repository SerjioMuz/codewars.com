def two_sum(numbers, target):
    for index,val in enumerate(numbers):
        print(val)
        if target-val in numbers[index+1:]:
            #print(target-val)
            return (numbers.index(val), numbers.index(target-val,numbers.index(val)+1))
            break



    #return((numbers.index(val), numbers.index(target-val)) break  for val in numbers if target-val in numbers)







print(two_sum([-8,7,3,4,5,6,7,-8,9,10,11],6))