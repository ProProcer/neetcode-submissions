class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = sorted(range(len(nums)), key = lambda i : nums[i])
        i = 0
        j = len(nums) -1
        while True:
            if nums[indices[i]] + nums[indices[j]] == target:
                if indices[i] < indices[j]:
                    return [indices[i], indices[j]]
                else:
                    return [indices[j], indices[i]]
            elif nums[indices[i]] + nums[indices[j]] > target:
                j -= 1
            else:
                i += 1
            
