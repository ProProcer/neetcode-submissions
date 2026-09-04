class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if num in nums[i + 1 : len(nums)]:
                return True
        return False