# https://leetcode.com/problems/reverse-words-in-a-string/#/description
# would have been fun to implement the split, reverse and join by myself, but I am too old for that :-|
class Solution(object):
	def reverseWords(self, s):
		if (s is None):
			return False

		strSplit = s.split()
		strSplit.reverse()

		return ' '.join(strSplit)


solution = Solution()
print(solution.reverseWords("the sky is blue"))