#https://youtu.be/ev0JrFgPO4E?si=mag8vJlcQS8AZ4Cc
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
five=Node("five")
three=Node("three")
two=Node("two")
nine=Node("nine")
four =Node("four")
eight=Node("eight")
one=Node("one")
six=Node("six")
ten=Node("ten")
five.left=three
three.left=two
three.right=nine
five.right=four
four.left=eight
eight.left=one
eight.right=six
four.right=ten






def preorder(node):   # DFS method PreOrder  (Root ->Left ->Right)
    if node==None:
        return
    print(node.val,end=" ") #Root Node
    preorder(node.left) # Left Node
    preorder(node.right) # Right Node

# print(preorder(five))


# TC-->(O(N))
# SC-->(O(H)) H is the Height


def inorder(node):   # DFS method InOrder  (Left ->Root ->Right)
    if node==None:
        return
    inorder(node.left) # Left Node
    print(node.val,end=" ") # Root Node
    inorder(node.right) # Right Node

# print(inorder(five))


def postorder(node):   # DFS method InOrder  (Left ->Right ->Root)
    if node==None:
        return
    postorder(node.left) # Left Node
    postorder(node.right) # Right Node
    print(node.val,end=" ") # Root Node

print(postorder(five))




    