'''
Write a Python function to insert a value into a binary search tree. The function should take the root of the tree and the value to be inserted as parameters.
'''
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

root = None
root = insert(root, 35)
root = insert(root, 100)
root = insert(root, 10)
root = insert(root, 55)
root = insert(root, 75)

print()
display(root)