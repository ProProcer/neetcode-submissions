class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for n in nums:
            num_dict[n] = 1 + num_dict.get(n, 0)
        print(num_dict)
        for i, x in enumerate(nums):
            num_dict[x] -= 1
            if num_dict.get(target - x, 0) > 0:
                break

        for j in range(i + 1, len(nums)):
            if nums[j] == target - x:
                return [i, j]

            