class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dfs = [False] * len(nums)
        dfs[0] = True
        for i in range(len(nums)):
            if not dfs[i]:
                continue
            
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dfs[j] = True
            
        return dfs[-1]