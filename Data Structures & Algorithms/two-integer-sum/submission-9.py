class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in set(nums[0 : i] + nums[i + 1 : len(nums)]):
                break
        for j in range(i + 1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]