# https://leetcode.com/problems/valid-parentheses/#/description
class Solution(object):
	def isValid(self, s):
		dictmap = { ')': '(', ']': '[', '}': '{'}
		stack = []

		if (s is None or len(s) is 0 or len(s) % 2 is not 0):
			return False

		for index in range(0, len(s)):
			if (s[index] in dictmap.keys()):
				if (len(stack) is 0 or dictmap[s[index]] != stack[len(stack) - 1]):
					return False
				else:
					stack.pop()
			else :
				stack.append(s[index])

		if (len(stack) is 0):
			return True
		else:
			return False



solution = Solution()
print(solution.isValid("({})"))