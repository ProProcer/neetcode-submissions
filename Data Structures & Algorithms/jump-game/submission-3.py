class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = 0
        for i in range(len(nums) - 1):
            fuel = max(fuel, nums[i])
            if fuel == 0:
                return False
            fuel -= 1
        return True