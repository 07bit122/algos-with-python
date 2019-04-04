class Solution(object):
    def maxProfit(self, prices):
        max_diff = 0

        if(len(prices) == 0):
            return 0
        
        min_price = prices[0]

        for price in prices:
            if (price < min_price):
                min_price = price
            elif (price - min_price > max_diff):
                max_diff = price - min_price
        return max_diff


solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([2,1,4]))