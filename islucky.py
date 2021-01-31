def isLucky(n):
    sum1= 0
    sum2= 0
    n= str(n)
    length=len(n)
    print(length)
    
    for i in range(0,int(length/2)):
        sum1+=int(n[i])
    print(sum1)
    for i in range(int((length/2)),len(n)):
        sum2+=int(n[i])
    print(sum2)
    if(sum1==sum2):
        return True
    return False

n=1230
isLucky(n)        

