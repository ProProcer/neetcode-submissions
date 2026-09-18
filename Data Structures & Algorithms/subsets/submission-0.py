class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        curr_list = []
        def helper(idx):
            if idx == len(nums):
                return result.append(curr_list[:])
            
            curr_list.append(nums[idx])
            helper(idx + 1)
            curr_list.pop()
            helper(idx + 1)
        helper(0)
        return result
        