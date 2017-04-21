# longest common subsequence
# solved using recursion
class Solution(object):
	def LCS(self, A, B, x, y):

		if (x is 0 or y is 0):
			return 0
		elif (A[x-1] == B[y-1]):
			return 1 + self.LCS(A, B, x-1, y-1)
		else:
			return max(self.LCS(A, B, x-1, y), self.LCS(A, B, x, y-1))


solution = Solution()
stringA = 'ABCDGH'
stringB = 'AEDFHR'
print(solution.LCS(stringA, stringB, len(stringA), len(stringB)))