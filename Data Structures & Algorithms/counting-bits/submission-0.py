class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        
        for i in range(1, n + 1):
            if (i | (i - 1)) - (i - 1) == len(result):
                result.append(1)
                continue
            result.append(result[(i | (i - 1)) - (i - 1)] + result[i & (i - 1)])
        return result