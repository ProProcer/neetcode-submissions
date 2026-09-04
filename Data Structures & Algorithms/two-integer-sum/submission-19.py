class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder_dict = {}
        for i, n in enumerate(nums):
            if n in remainder_dict:
                return [remainder_dict[n], i]
            remainder_dict[target - n] = i

            