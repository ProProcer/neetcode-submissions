class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            fewest = float('inf')

            for c in coins:
                if amount - c < 0:
                    continue
                else:
                    
                    fewest = min(fewest, 1 + helper(amount - c))
            cache[amount]  = fewest
            return fewest

        result = helper(amount)
        if result == float('inf'):
            return -1
        else:
            return result