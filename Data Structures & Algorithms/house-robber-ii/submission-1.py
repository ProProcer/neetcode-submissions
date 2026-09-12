class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        def max_rob(start_idx, end_idx):
            if end_idx + 1 - start_idx == 1:
                return nums[start_idx]
            if end_idx + 1 - start_idx == 2:
                return max(nums[start_idx], nums[start_idx + 1])
            rob1, rob2 = nums[start_idx], max(nums[start_idx], nums[start_idx + 1])
            for i in range(start_idx + 2, end_idx + 1):
                temp = rob2
                rob2 = max(rob2, rob1 + nums[i])
                rob1 = temp
            return rob2
        return max(max_rob(1, len(nums) - 1), nums[0] + max_rob(2, len(nums) - 2))
        