# longest increasing subsequence
# solved using tablulation

class Solution(object):
	def LIS(self, numList):
		n = len(numList)
		LISTCounts = [1] * n

		for i in range(1, n):
			for j in range(0, i):
				if(numList[i] > numList[j] and LISTCounts[i] < LISTCounts[j] + 1):
					LISTCounts[i] = LISTCounts[j] + 1


		return max(LISTCounts)

solution = Solution()
print(solution.LIS((10, 22, 9, 33, 21, 50, 41, 60)))