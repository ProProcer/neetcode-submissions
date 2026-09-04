class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = set()
        for num in nums:
            if num in items:
                return True
            else:
                items.add(num)
        return False