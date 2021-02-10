def climbingStairs(n):
    lst=[0,1,2]
    for i in range (3,n+1):
       sum=lst[i-1]+lst[i-2]
       lst.append(sum)
    return lst[n]

print(climbingStairs(10))

