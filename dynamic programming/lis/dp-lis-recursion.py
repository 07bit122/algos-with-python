# longest increasing subsequence
# solved using recursion
class Solution(object):

	def __init__(self):
		self.max_length = 1

	def LIS(self, numList, endIndex):
		current_list_length = 1
		print('called with endIndex ' + str(endIndex))
		for i in range(0, endIndex - 1):
			print('calling LIST with endIndex ' + str(endIndex) + ' and i being ' + str(i))
			sub_problem_length = self.LIS(numList, i)

			if (numList[i] < numList[endIndex - 1] and current_list_length < (sub_problem_length + 1)):
				current_list_length = sub_problem_length + 1

		if (self.max_length < current_list_length):
			self.max_length = current_list_length

		return current_list_length


solution = Solution()
array = (3, 10, 2, 1, 20)
solution.LIS(array, len(array))
print(solution.max_length)