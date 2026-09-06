class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        best_area = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            best_area = max(best_area, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return best_area

    