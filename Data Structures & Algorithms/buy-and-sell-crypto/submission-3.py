class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_prof = 0
        for p in prices:
            max_prof = max(max_prof, p - min_buy)
            min_buy = min(min_buy, p)
        return max_prof
