class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        nums = sorted(nums_set)
        longest_count = 1
        contender_count = 1
        for n in nums:
            if n + 1 in nums_set:
                contender_count += 1
                continue
            elif longest_count < contender_count:
                longest_count = contender_count
            contender_count = 1

        return longest_count  

