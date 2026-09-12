class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pref = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = curr
            curr = max(nums[i] + pref, curr)
            pref = temp
        return curr