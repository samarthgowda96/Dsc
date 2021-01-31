def candies(n, m):
    num= m//n
    str(n)
    res=0
    for i in range(1,n):
        res= res+num*i
    return res
n=3
m=10
print(candies(n,m))