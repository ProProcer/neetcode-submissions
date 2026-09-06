class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                max_prof = max(max_prof, prices[r] - prices[l])
            r += 1
        return max_prof