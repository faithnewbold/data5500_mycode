'''
2. Implement a Python function to search for a value in a binary search tree. The method should take the root of the tree and the value to be searched as parameters. It should return True if the value is found in the tree, and False otherwise.
'''

#starting with my code from easy.py to create the tree
from print_tree import *

# A Binary Tree Node

class TreeNode:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return TreeNode(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

def find(root, find_key): #used to find if a value is in the tree
    if root is None:
        return False  
    
    if root.key == find_key:
        return True  

    if find_key < root.key:
        return find(root.left, find_key)  
    else:
        return find(root.right, find_key)

root = None
root = insert(root, 50)
root = insert(root, 60)
root = insert(root, 10)
root = insert(root, 35)
root = insert(root, 75)

print()
display(root)

print()
print("Is the value found?:", find(root, 35)) #should return True
print("Is the value found?:", find(root, 65)) #should return False