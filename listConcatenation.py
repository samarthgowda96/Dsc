def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res

lst1=[1,2,3]
lst2=[2,2,4]
print(listsConcatenation(lst1,lst2))