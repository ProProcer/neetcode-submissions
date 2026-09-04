class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_dict = {}
        for i, n in enumerate(nums):
            if target - n in prev_dict:
                return [prev_dict[target -n ], i]
            prev_dict[n] = i

            