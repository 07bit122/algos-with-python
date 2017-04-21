# longest increasing subsequence
# solved using memoization
class Solution(object):

	def __init__(self):
		self.max_length = 1
		# all the LIS start at index 0.
		# we will have the dict with keys being 'x' and values being LIS length
		self.memoizeLIS = {}

	def LIS(self, numList, endIndex):
		current_list_length = 1

		for i in range(0, endIndex - 1):
			if (i not in self.memoizeLIS.keys()):
				self.memoizeLIS[i] = self.LIS(numList, i)
			sub_problem_length = self.memoizeLIS[i]

			if (numList[i] < numList[endIndex - 1] and current_list_length < (sub_problem_length + 1)):
				current_list_length = sub_problem_length + 1

		if (self.max_length < current_list_length):
			self.max_length = current_list_length

		return current_list_length


solution = Solution()
array = (10, 22, 9, 33, 21, 50, 41, 60)
solution.LIS(array, len(array))
print(solution.max_length)