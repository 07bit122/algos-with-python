class Solution(object):
    def isPalindrome(self, x):
        # if the number is negative, the number cannot be a palindrome
        # given the example in problem description
        if (x < 0):
            return False
        else:
            return self.checkPalindrome(x)
    
    def checkPalindrome(self, x):
        y = 0
        match_with = x
        while (x):
            a = x % 10
            x = x / 10
            y = a + (y * 10)

        if (match_with == y):
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(10))