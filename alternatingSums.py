def alternatingSums(a):
    Team1=[]
    Team2=[]
    length= len(a)
    str(length)
    for i in range(0,length):
        if(i%2!=0):
            Team2.append(a[i])
            continue
        elif(i%2==0):
            Team1.append(a[i])
            continue
    Team1Len=len(Team1)
    str(Team1Len)
    sum1=0 
    sum2=0
    Team2Len=len(Team2)
    str(Team2Len)
    for i in range(0,Team1Len):
        sum1 = sum1+Team1[i]
    for i in range(0,Team2Len):
        sum2= sum2+Team2[i]
    return sum1,sum2    

        

a=[1,2,69,96,1,2,1]
print(alternatingSums(a))