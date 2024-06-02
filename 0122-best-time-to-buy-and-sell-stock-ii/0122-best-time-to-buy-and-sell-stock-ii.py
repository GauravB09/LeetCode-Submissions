class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        n = len(prices)
        dp = [0 for i in range(n)]
        for i in range(1,n):
            dp[i] = max(dp[i-1], dp[i-1]+(prices[i]-prices[i-1]), prices[i]-min_so_far)
        return dp[n-1]