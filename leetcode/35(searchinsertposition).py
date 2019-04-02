class Solution(object):
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)/2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l

solution = Solution()
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1,3,5,6], 2))