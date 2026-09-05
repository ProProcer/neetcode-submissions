class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [nums[0]] + [1] * (len(nums) - 1)
        right_prods = [1] * (len(nums) - 1) + [nums[len(nums) - 1]]
        for i, j in zip(range(1, len(nums)), range(len(nums) - 2, -1, -1)):
            left_prods[i] = left_prods[i - 1] * nums[i]
            right_prods[j] = right_prods[j + 1] * nums[j]

    
        result = [right_prods[1]]
        for i in range(1, len(nums) - 1):
            result.append(left_prods[i - 1] * right_prods[i + 1])
        result.append(left_prods[len(nums) - 2])
        return result
        