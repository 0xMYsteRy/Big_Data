# Python Program to introduce Binary Tree
# A class that represents an individual node a binary tree.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Create Root
root = Node(1)
'''
Following is the tree after above statment
         1
       /   \
      None None 
'''

root.left = Node(2)
root.right = Node(3)
'''
2 and 3 become left and right children of (1)
          1
       /     \
     2         3
   /  \      /   \
 None None None None    
'''

root.left.left = Node(4)


