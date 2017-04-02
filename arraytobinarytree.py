# Simple Binary Tree Construction From Array.
# Tons of opportunities to improve on this one.
# Currently, code assumes the binary tree is complete. Cannot handle cases where a level could be incomplete
class TreeNode(object):
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

class BinaryTree(object):
	def ArrayToBinaryTree(self, array):

		queue = []

		if (array is None):
			return False

		# self will contain the tree data structure
		self.root = TreeNode(array[0])
		# queue is to iterate over the parent nodes for the binary tree
		queue.append(self.root)

		for index in range(1, len(array) - 1, 2):
			parent = queue.pop(0)

			leftChild = TreeNode(array[index])
			rightChild = TreeNode(array[index + 1])

			queue.append(leftChild)
			queue.append(rightChild)

			parent.left = leftChild
			parent.right = rightChild

		return self.root

	def inOrderTraversal(self, root):
		if (root):
			self.inOrderTraversal(root.left)
			print(root.data)
			self.inOrderTraversal(root.right)

obj = BinaryTree()
root = obj.ArrayToBinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
obj.inOrderTraversal(root)