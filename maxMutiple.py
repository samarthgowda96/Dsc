import math
def maxMultiple(divisor, bound):
    res= (bound%divisor)
    print(res)
    return bound - (bound % divisor)

print(maxMultiple(10,50))