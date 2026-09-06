class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res= []
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) -1
            while l < r:
                sum_num = nums[l] + nums[r] + nums[i]
                if sum_num < 0 or (nums[l -1] == nums[l] and l - i > 1):
                    l += 1
                elif sum_num > 0 or (r + 1 < len(nums) and nums[r+1] == nums[r]):
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+= 1
                    r -= 1

        return res
