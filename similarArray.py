def areSimilar(a, b):
    lenA= len(a)
    joinA=''.join(a)
    joinB=''.join(b)

  
    def swap(t,s,e):
        res= t.slice()
        res[s]=t[e]
        res[e]=t[s]
        return res
    if(joinA==joinB):
        return True
    
    for i in range(0,lenA-1):
        for j in range(0,lenA):
            if(swap(a,i,j).join()==joinB):
                return True

    return False
    

print(areSimilar(['1','3','3','6'],['1','3','3','4']))