class postorder:
    def __init__(self,data):
        self.data=data
        self.left= None
        self.right=None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = postorder(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right=postorder(data)
                else:
                    self.right.insert(data)
        else:
            self.data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()

    def postordertraversal(self,tree):
        stack=[]
        if tree:
            stack= stack+self.postordertraversal(tree.left)
            stack=stack+self.postordertraversal(tree.right)
            stack.append(tree.data)
        return stack

if __name__=="__main__":
    tree= postorder(78)
    tree.insert(30)
    tree.insert(1)
    tree.insert(10)
    tree.insert(69)
    tree.insert(4)
    tree.insert(51)
    tree.printtree()
    print(tree.postordertraversal(tree))