#https://youtu.be/qp2ct1cOgdM?si=MZv3ACKIIMbOGhc-

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
drinks=Node("drinks")
hot=Node("hot")
cold=Node("cold")
coffee=Node("coffee")
tea=Node("tea")
cola=Node("cola")
fanta=Node("fanta")

hot.left=coffee
hot.right=tea
cold.left=cola
cold.right=fanta
drinks.left=hot
drinks.right=cold


print(drinks.left.right.val) # Left of Drinks is hot and hot right is Tea