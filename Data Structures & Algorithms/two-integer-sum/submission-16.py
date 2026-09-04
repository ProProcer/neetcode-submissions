class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {n : i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            if num_dict.get(target - n, i) != i:
                return [i, num_dict.get(target - n)]

            