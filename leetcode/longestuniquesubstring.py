# https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		initialposition = 0
		longestlength = 0
		memoizeMap = {}

		for i in range(len(s)):
			if (s[i] in memoizeMap and initialposition <= memoizeMap[s[i]]):
				initialposition = memoizeMap[s[i]] + 1
			else:
				longestlength = max(longestlength, i - initialposition + 1)

			memoizeMap[s[i]] = i

		return longestlength

solution = Solution();
print(solution.lengthOfLongestSubstring('aqmpcsrumjjufu'))