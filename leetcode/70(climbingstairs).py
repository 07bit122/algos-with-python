class Solution(object):

    def __init__(self):
        self.count_dict = {
            0: 1,
            1: 1
        }
    # this is also another form of a fibonacci problem
    def climbStairs(self, n):
        for x in range (2, n+1, 1):
            self.count_dict[x] = self.count_dict[x-1] + self.count_dict[x-2]
            del self.count_dict[x-2]
        return self.count_dict[n]

"""     def __init__(self) :
        self.total_possibilities = 0
    
    def climbStairs(self, n):
        if (n <= 0):
            return self.total_possibilities
        else:
            self.countPossibilities(n)
            return self.total_possibilities
    
    def countPossibilities(self, current_number):
        if (current_number > 0):
            self.countPossibilities(current_number - 1)
            self.countPossibilities(current_number - 2)
        elif (current_number == 0):
            self.total_possibilities += 1
            return
        else:
            return """

solution = Solution()
print(solution.climbStairs(35))