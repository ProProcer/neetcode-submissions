class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {n : i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            j = num_dict.get(target - n, i)
            if j != i:
                return [i, j]

            