#https://youtu.be/tRhWzxU-oH0?si=QXT9-kfQ_F3mtdZA

from collections import deque

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






def levelorder(node):
    result = []          # Stores node values in traversal order
    queue = deque([])    # FIFO queue: first node added is processed first

    queue.append(node)   # Start BFS by adding the root node

    while len(queue) != 0:  # Continue until no nodes remain
        e = queue.popleft()  # Remove the front node from the queue
        result.append(e.val) # Visit the node and store its value

        # Add left child first, so it is processed before the right child
        if e.left is not None:
            queue.append(e.left)

        # Add right child to process it after the left child
        if e.right is not None:
            queue.append(e.right)

    return result  # Return values in level-order



print(levelorder(five))

#TC--> O(N)
#SC --> O(N)

