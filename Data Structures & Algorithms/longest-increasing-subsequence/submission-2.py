class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j] > dp[i]:
                        dp[i] = dp[j]
            dp[i] += 1
        
        return max(dp)