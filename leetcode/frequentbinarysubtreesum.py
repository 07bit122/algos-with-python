# https://leetcode.com/problems/most-frequent-subtree-sum/#/description
class Solution(object):

	def findFrequentTreeSum(self, root):
		if root == None: return []

		subTreeSumMap = {}

		def getSum(node):
		    if node == None: return 0
		    s = node.val + getSum(node.left) + getSum(node.right)
		    subTreeSumMap[s] = subTreeSumMap.get(s, 0) + 1
		    return s

		getSum(root)
		maxSum = max(subTreeSumMap.values())
		return [k for k,v in subTreeSumMap.items() if v == maxSum]