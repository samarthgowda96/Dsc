class binarytree:
    #initialization or constructor
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data



    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = binarytree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = binarytree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data),
        if self.right:
            self.right.printtree()

    def deletetree(self,tree):
        if tree:
            self.deletetree(tree.left)
            self.deletetree(tree.right)
            tree.left=None
            tree.right=None
        else:
            tree=None

    #find max depth
    def maxdepth(self,tree):
        if tree==None:
            return 0
        return max(self.maxdepth(tree.left), self.maxdepth(tree.right))+1
        
if __name__=="__main__":
    tree= binarytree(20)
    tree.insert(3)
    tree.insert(1)
   
    
    tree.insert(4)
    tree.insert(5)
    """ tree.insert(30)
    tree.insert(40)
    tree.insert(50) """
    tree.insert(60)
    tree.insert(70)
 
   

    tree.printtree()
    #print(tree.deletetree(tree))
    print(tree.maxdepth(tree))
   



    
    
    

