class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_sorted = sorted([(p, i) for p, i in zip(prices, range(len(prices)))])

        max_prof = 0
        prev_i = -1
        i = -1
        while i < len(prices) - 1:
            p, idx = price_sorted.pop()
            if idx < i:
                continue
            i = idx
            for j in range(i - 1, prev_i, -1):
                max_prof = max(prices[i] - prices[j], max_prof)
            prev_i = i
        return max_prof