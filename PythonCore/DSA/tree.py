#Creating a tree node
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#performing inorder operation
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
#Performing pre order operation 
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
#performing post order operation
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    print("Inorder")
    inorder(root)
    print("Preorder")
    preorder(root)
    print("Postorder")
    postorder(root)

if __name__=="__main__":
    main()