class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [None] * len(nums)
        
        
        def dfs(idx):
            if cache[idx]:
                return cache[idx]
            if idx == 0:
                cache[0] = nums[0]
                return nums[0]
            if idx == 1:
                cache[1] = max(nums[0], nums[1])
                return cache[1]
            cache[idx] = max(nums[idx] + dfs(idx - 2), dfs(idx -1))
            return cache[idx]
        return dfs(len(nums) - 1)
