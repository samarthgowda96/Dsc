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
        
if __name__=="__main__":
    root = binarytree(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.printtree()


    
    
    

