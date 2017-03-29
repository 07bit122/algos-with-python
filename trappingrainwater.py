# https://leetcode.com/problems/trapping-rain-water/#/description
class Solution(object):
	def trap(self, height):
		capacity = 0
		startingPoint = 0

		if (len(height) == 0):
			return 0

		# for each point on the graph,
		# find the left most tallest and right most tallest
		# find the shortest of the lmax and rmax
		# do a difference with the current index position's value
		# that should give the rain water that would be trapped at a given point
		for index in range(0, len(height)-1):
			leftTallestIndex = self.findLeftTallest(index, height)
			rightTallestIndex = self.findRightTallest(index, height)
			if (leftTallestIndex == index or rightTallestIndex == index):
				continue
			capacity += min(height[leftTallestIndex], height[rightTallestIndex]) - height[index]

		# return result
		return capacity

	def findLeftTallest(self, index, height):
		maxindex = index
		for i in range(0, index):
			if(height[i] > height[maxindex]):
				maxindex = i
		return maxindex

	def findRightTallest(self, index, height):
		maxindex = index
		for i in range(index + 1, len(height)):
			if(height[i] > height[maxindex]):
				maxindex = i
		return maxindex

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap([0,2,0]))
print(solution.trap([4,2,3]))
print(solution.trap([0,1,0,2,1,0,1,3]))