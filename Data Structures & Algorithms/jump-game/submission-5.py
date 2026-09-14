class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) -1:
                return True
            if max_reach == i:
                return False
        