class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(n):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coins[j]])
        return dp[amount] if dp[amount] != amount + 1 else -1
        