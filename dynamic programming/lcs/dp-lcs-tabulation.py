# longest common subsequence
# solved using tabulation

class Solution(object):
	def LCS(self, A, B, x, y):
		tabulation = []

		for i in range(0, x + 1):
			array = [None] * (y + 1)
			tabulation.append(array)

		for i in range(0, x + 1):
			for j in range(0, y + 1):
				if (i == 0 or j == 0):
					tabulation[i][j] = 0
				elif (A[i-1] == B[j-1]):
					tabulation[i][j] = 1 + tabulation[i-1][j-1]
				else:
					tabulation[i][j] = max(tabulation[i-1][j], tabulation[i][j-1])

		return tabulation[x][y]

solution = Solution()
A = 'AGGTAB'
B = 'GXTXAYB'
print(solution.LCS(A, B, len(A), len(B)))