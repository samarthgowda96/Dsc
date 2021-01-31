def allLongestStrings(inputArray):
    arr = inputArray
    strSize=[]
    for i in range(0,len(arr)):
        strSize.append(len(arr[i]))
    strSize.sort(reverse=True)
    maxSize= max(strSize)
    resStr=[]
    for i in arr:
        if(len(i)==maxSize):
            resStr.append(i)
    return resStr
inputArray = ['ssssss','ssss','sss','sae','23','qwqwqwqwqwq']
print(allLongestStrings(inputArray))


