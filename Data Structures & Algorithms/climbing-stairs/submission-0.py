from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        answer = 0
        prev_prev = 1
        prev = 2
        for i in range(2, n):
            answer = prev + prev_prev
            prev_prev = prev
            prev = answer
        return answer