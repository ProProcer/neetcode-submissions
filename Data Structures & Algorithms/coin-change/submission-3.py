class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i-c])
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]