class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp_max = nums[0]
        dp_min = nums[0]
        max_num = dp_max
        for i in range(1, len(nums)):
            temp_max = dp_max
            temp_min = dp_min
            dp_max = max((temp_min * nums[i], temp_max * nums[i], nums[i]))
            dp_min = min((temp_min * nums[i], temp_max * nums[i], nums[i]))
            max_num = max(dp_max, max_num)
        
        return max_num
        
