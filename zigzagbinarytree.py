# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/#/description
class Solution(object):
	def __init__(self):
		# have 2 val structures that we alternate upon
		# queue does a first in first out
		# stack does a last in first out
		self.queue = []
		self.stack = []
		self.end_result = []

	def zigzagLevelOrder(self, root):
		# base test case to make sure we don't proceed further if the root
		# is empty
		if (root is None):
			self.end_result = []
			return self.end_result

		# if root is the only element in the tree and it has no sub-nodes
		# return the result after pushing the root into the result array
		if (root.left is None and root.right is None):
			self.end_result.append([root.val])
			return self.end_result

		self.queue.append(root)
		self.processqueue()
		return self.end_result

	# a function to check if the queue and stack, the data structures that we
	# iterate upon are empty. Return True if they are empty, so that we know
	# when to end the recursive stack and queue processing
	# basically this helps in serving the purpose of validating the basecase
	# for a recursion
	def checkEmptyDS(self):
		if (len(self.queue) is 0 and len(self.stack) is 0):
			return True

	def processqueue(self):
		if (self.checkEmptyDS() is True):
			return
		dequeueList = []
		while(len(self.queue) > 0):
			currentNode = self.queue.pop(0)

			dequeueList.append(currentNode.val)

			# when processing the queue, the sub-nodes should be processed
			# left first and right next
			if (currentNode.left is not None):
				self.stack.append(currentNode.left)
				print('appending ' + str(currentNode.left.val) + ' into stack')
			if (currentNode.right is not None):
				self.stack.append(currentNode.right)
				print('appending ' + str(currentNode.right.val) + ' into stack')

		self.end_result.append(dequeueList)
		self.processstack()

	def processstack(self):
		if (self.checkEmptyDS() is True):
			return
		dequeueList = []
		while(len(self.stack) > 0):
			currentNode = self.stack.pop()

			dequeueList.append(currentNode.val)

			# when processing the stack, the sub-nodes should be processed
			# right first and left next
			if(currentNode.right is not None):
				self.queue.append(currentNode.right)
				print('appending ' + str(currentNode.right.val) + ' into queue')
			if (currentNode.left is not None):
				print('appending ' + str(currentNode.left.val) + ' into queue')
				self.queue.append(currentNode.left)

		self.end_result.append(dequeueList)
		# after the queue is populated with sub-nodes reverse it, so that
		# they appear in the alternate order for the zigzag
		self.queue.reverse()
		self.processqueue()