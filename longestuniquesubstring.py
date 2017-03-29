# https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		initialposition = 0
		longestlength = 0

		while(initialposition >= 0):
			usedCharacters = {}
			longestlengthinthisiteration = 0
			completedStringParsing = True
			for index in range(initialposition, len(s)):
				if(s[index] not in usedCharacters):
					usedCharacters[s[index]] = index
					longestlengthinthisiteration += 1
				else:
					initialposition = usedCharacters[s[index]] + 1
					completedStringParsing = False
					if (longestlengthinthisiteration > longestlength):
						longestlength = longestlengthinthisiteration
					break
			if (completedStringParsing is True):
				if (longestlengthinthisiteration > longestlength):
					longestlength = longestlengthinthisiteration
				initialposition = -1

		return longestlength

solution = Solution();
print(solution.lengthOfLongestSubstring('aqmpcsrumjjufu'))