
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        path = []
        result = []
        def backtrack(sum_, index):
            if sum_ == target:
                result.append(path[:])
                return 
            for i in range(index, len(nums)):
                temp_sum = nums[i] + sum_
                if temp_sum > target:
                    break
                path.append(nums[i])     
                backtrack(temp_sum, i)
                path.pop()
        backtrack(0, 0)
        return result
