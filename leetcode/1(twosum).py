# https://leetcode.com/problems/two-sum/#/description
class Solution(object):
    def twoSum(self, nums, target):
        expected_b_map = {}
        for num in range(0, len(nums)):

            if (nums[num] in expected_b_map.keys()):
                return [expected_b_map[nums[num]], num]
            else:
                expected_b_map[target - nums[num]] = num
        return []

a = Solution()
print(a.twoSum([3,4,7,10], 11))