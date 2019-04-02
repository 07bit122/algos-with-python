class Solution(object):
    def longestCommonPrefix(self, strs):
        # iterate over the smallest string
        if (len(strs) == 0):
            return ''
        length = len(strs[0])
        string_to_iterate = strs[0]
        longest_prefix = ''
        for i in range(len(strs)):
            if (length > len(strs[i])):
                length = len(strs[i])
                string_to_iterate = strs[i]
        
        for i in range(len(string_to_iterate)):
            check_flag = True
            for j in range(len(strs)):
                strs_j = strs[j]
                if (string_to_iterate[i] == strs_j[i]):
                    check_flag = True
                else:
                    check_flag = False
                    break
            if (check_flag):
                longest_prefix += string_to_iterate[i]
            else:
                break
        return longest_prefix

solution = Solution()
# print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["aab","aab"]))