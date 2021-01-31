def largestNumber(n):
    temp=0
    for i in range(0,n):
        temp=temp+9*pow(10,i)
    return temp
n=10
largestNumber(n)