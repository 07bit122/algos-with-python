# edit distance to convert str 1 into str 2
# solved using recursion

class Solution(object):
	def editDistance(self, A, B, x, y):

		if (x is 0):
			return y

		if (y is 0):
			return x


		if (A[x-1] == B[y-1]):
			return self.editDistance(A, B, x-1, y-1)
		else:
			return 1 + min(
				self.editDistance(A, B, x-1, y),
				self.editDistance(A, B, x, y-1),
				self.editDistance(A, B, x-1, y-1)
			)


solution = Solution()
A = 'sunday'
B = 'saturday'
print(solution.editDistance(A, B, len(A), len(B)))