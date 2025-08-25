class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
        return maxProfit

#Time complexity: O(n)
#Space complexity: O(1)


