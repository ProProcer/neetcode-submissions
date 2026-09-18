class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        left_max[0] = height[0]
        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
            right_max[-i -1] = max(right_max[-i], height[-i-1])
        volume = 0
        for i, h in enumerate(height):
            volume += max(min(left_max[i], right_max[i]) - h, 0)
        return volume