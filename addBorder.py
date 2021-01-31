def addBorder(picture):
    startEnd=""
    End=""
    firstPicLen=len(picture[0])
    for i in range(0,firstPicLen+2):
        startEnd=startEnd+"*"
    
    
    finalArray=[]
    finalArray.append(startEnd)
    
    picLen=len(picture)
    for i in range(0,picLen):
        finalArray.append("*"+picture[i]+"*")

    for i in range(0,firstPicLen+2):
        End=End+"*"
    finalArray.append(End)
    print(finalArray)







picture = ["abc","ded"]

addBorder(picture)