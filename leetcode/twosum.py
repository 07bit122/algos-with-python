# https://leetcode.com/problems/two-sum/#/description
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        counter = 0
        for num in nums:
            if(num in dict.keys() and len(dict[num]) >= 1):
        	    dict[num].append(counter)
            else:
                dict[num] = [counter]
            counter += 1
        print(dict)
        for key in dict.keys():
            difference = target - key
            if (difference in dict.keys()):
                if (len(dict[difference]) > 1):
            	    return [dict[difference][0], dict[difference][1]]
                elif (difference != key and len(dict[difference]) == 1):
                    return [dict[key][0], dict[difference][0]]

a = Solution()
print(a.twoSum([3,3], 6))