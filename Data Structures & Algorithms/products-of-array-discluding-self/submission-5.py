class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeros_count = 0
        zeros_idx = None
        for i, n in enumerate(nums):
            if n == 0:
                zeros_count += 1
                if zeros_count >= 2:
                    return [0] * len(nums)
                zeros_idx = i
            else:
                total_product *= n

        if zeros_idx is not None:
            result = [0] * len(nums)
            result[zeros_idx] = total_product
            return result
        

        return [total_product // n for n in nums]