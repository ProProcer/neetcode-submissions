from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        count= defaultdict(int)
        result = []
        for n in nums:
            count[n]+=1
        
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums [i-1]:
                continue
            for j in range(i + 1, len(nums)):
                
                if j-i > 1 and nums[j] == nums[j-1]:
                    continue
                target = -nums[i] -nums[j]
                if target < nums[j]:
                    continue
                count[nums[j]] -= 1
                if count[target] >0:
                    result.append([nums[i], nums[j], target])
                count[nums[j]] += 1
            if target < nums[j]:
                continue 
        return result

