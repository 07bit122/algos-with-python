# https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description
from random import *

class Solution(object):
	def letterCombinations(self, digits):
		if ('1' in digits):
			return False;

		if(len(digits) is 0):
			return []

		keyMap = {
			2: ['a', 'b', 'c'],
			3: ['d', 'e', 'f'],
			4: ['g', 'h', 'i'],
			5: ['j', 'k', 'l'],
			6: ['m', 'n', 'o'],
			7: ['p', 'q', 'r', 's'],
			8: ['t', 'u', 'v'],
			9: ['w', 'x', 'y', 'z'],
		}

		expectedCombinations = 1
		for digit in map(int, digits):
			expectedCombinations *= len(keyMap[digit])

		calculatedCombinations = []
		while(len(calculatedCombinations) < expectedCombinations):
			combinationGenerated = ''

			for digit in map(int, digits):
				randInt = randint(0, len(keyMap[digit]) - 1)
				combinationGenerated += keyMap[digit][randInt]

			if combinationGenerated not in calculatedCombinations:
				calculatedCombinations.append(combinationGenerated)

		return calculatedCombinations;

solution = Solution()
print(solution.letterCombinations('2345'))