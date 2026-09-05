class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for n in set_nums:
            contender = 0
            if n - 1 in set_nums:
                continue
            while True:
                contender += 1
                if n + contender not in set_nums:
                    break
            if longest < contender:
                longest =contender
            
        return longest
