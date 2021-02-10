def square_digits(num):
    return ''.join(str(int(i)**2) for i in str(num))

num=8336
print(square_digits(num))