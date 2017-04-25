# edit distance to convert str 1 into str 2
# solved using tabulation
class Solution(object):
	def editDistance(self, A, B, x, y):
		tabulation = []

		for i in range(0, x + 1):
			array = [None] * (y + 1)
			tabulation.append(array)

		for i in range(0, x + 1):
			for j in range(0, y + 1):
				if (i is 0):
					tabulation[i][j] = j
				elif (j is 0):
					tabulation[i][j] = i
				elif (A[i-1] == B[j-1]):
					tabulation[i][j] = tabulation[i-1][j-1]
				else:
					tabulation[i][j] = 1 + min(
						tabulation[i-1][j],
						tabulation[i][j-1],
						tabulation[i-1][j-1]
					)

		return tabulation[x][y]

solution = Solution()
A = 'sunday'
B = 'saturday'
print(solution.editDistance(A, B, len(A), len(B)))