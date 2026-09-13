class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp_max = nums[0]
        dp_min = nums[0]
        max_num = dp_max
        for i in range(1, len(nums)):
            x = nums[i]
            dp_max, dp_min = (
                max((dp_min * x, dp_max * x, x)), 
                min((dp_min * x, dp_max * x, x))
            )
            max_num = max(dp_max, max_num)
        
        return max_num
        
