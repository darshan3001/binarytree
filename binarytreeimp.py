class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def PreOrderTraversal(self):
        print(self.data,end='---')
        if self.left:
            self.left.PreOrderTraversal()
        if(self.right):
            self.right.PreOrderTraversal()
    def PostOrderTraversal(self):
        if(self.left):
            self.left.PostOrderTraversal()
        if(self.right):
            self.right.PostOrderTraversal()
        print(self.data,end='---')
    def InOrderTraversal(self):
        if(self.left):
            self.left.InOrderTraversal()
        print(self.data,end='---')
        if(self.right):
            self.right.InOrderTraversal()
n=Node(1)
n.left=Node(2)
n.left.left=Node(3)
n.right=Node(4)
n.right.left=Node(10)
n.right.right=Node(11)
print('Inorder Traversal : ')
n.InOrderTraversal()
print('\nPreorder Traversal : ')
n.PreOrderTraversal()
print('\nPostorder Traversal : ')
n.PostOrderTraversal()