class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = sorted([(n, i) for i, n in enumerate(nums)])
        i = 0
        j = len(nums) -1
        while True:
            if indices[i][0] + indices[j][0] == target:
                return [min(indices[i][1], indices[j][1]), max(indices[i][1], indices[j][1])]
            elif indices[i][0] + indices[j][0] > target:
                j -= 1
            else:
                i += 1
            
