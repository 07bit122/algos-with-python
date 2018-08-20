# https://leetcode.com/problems/find-largest-value-in-each-tree-row/#/description
class Solution(object):
	def __init__(self):
		# have 2 val structures that we alternate upon for processing
		# each level of the binary tree
		# queue1 does a first in first out
		# queue2 does a first in first out as well
		self.queue1 = []
		self.queue2 = []
		self.end_result = []

	def largestValues(self, root):
		# base test case to make sure we don't proceed further if the root
		# is empty
		if (root is None):
			self.end_result = []
			return self.end_result

		# if root is the only element in the tree and it has no sub-nodes
		# return the result after pushing the root into the result array
		if (root.left is None and root.right is None):
			self.end_result.append(root.val)
			return self.end_result

		self.queue1.append(root)
		self.processqueue1()
		return self.end_result

	# a function to check if the queue1 and queue2, the data structures that we
	# iterate upon are empty. Return True if they are empty, so that we know
	# when to end the recursive queue2 and queue1 processing
	# basically this helps in serving the purpose of validating the basecase
	# for a recursion
	def checkEmptyDS(self):
		if (len(self.queue1) is 0 and len(self.queue2) is 0):
			return True

	def processqueue1(self):
		if (self.checkEmptyDS() is True):
			return
		treeLevelNodes = []
		while(len(self.queue1) > 0):
			currentNode = self.queue1.pop(0)

			treeLevelNodes.append(currentNode.val)

			if (currentNode.left is not None):
				self.queue2.append(currentNode.left)
			if (currentNode.right is not None):
				self.queue2.append(currentNode.right)

		self.end_result.append(max(treeLevelNodes))
		self.processqueue2()

	def processqueue2(self):
		if (self.checkEmptyDS() is True):
			return
		treeLevelNodes = []
		while(len(self.queue2) > 0):
			currentNode = self.queue2.pop(0)

			treeLevelNodes.append(currentNode.val)

			if(currentNode.left is not None):
				self.queue1.append(currentNode.left)
			if (currentNode.right is not None):
				self.queue1.append(currentNode.right)

		self.end_result.append(max(treeLevelNodes))
		self.processqueue1()