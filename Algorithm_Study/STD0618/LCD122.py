from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        mn = 10000
        for  i in range(len(prices) -1 ) :
            mn = min(mn, prices[i])
            if prices[i] > prices[i+1] :
                result += max(0, prices[i] - mn)
                mn = prices[i+1]
        result += max(0, prices[-1] - mn)
        return result

solution = Solution()
prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices))
prices = [1,2,3,4,5]
print(solution.maxProfit(prices))
prices = [7,6,4,3,1]
print(solution.maxProfit(prices))