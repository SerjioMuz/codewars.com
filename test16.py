def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))








res = square_digits(555)
print(res)