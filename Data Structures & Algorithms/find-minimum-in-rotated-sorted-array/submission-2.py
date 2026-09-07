class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        c = (l + r) //2 
        
        while nums[c -1] < nums[c] and l < r:
            if nums[c] < nums[0]:
                r = c - 1
            else:
                l = c + 1
            c = (r + l) // 2 
        return nums[c]
                
                
                
                

