import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count=0

for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j]>a[j+1]):
            count=count+1
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print("Array is sorted in",f'{count}', 'swaps.')
print("First Element:",a[0])
print("Last Element:",a[-1])
