class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) / 2
        diff =  total_sum - sum(nums)
        if diff:
            return int(diff)
        else:
            return 0