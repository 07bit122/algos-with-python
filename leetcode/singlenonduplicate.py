# https://leetcode.com/problems/single-element-in-a-sorted-array/#/description
class Solution(object):
	def singleNonDuplicate(self, nums):
		if(len(nums) == 0):
			return False
		for i in range(0,len(nums)-1,2):
			if(nums[i] - nums[i + 1] != 0):
				return nums[i]
		return nums[len(nums)-1]

solution = Solution()
print(solution.singleNonDuplicate([1,1,2]))