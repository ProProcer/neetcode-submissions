from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            if r - l + 1 > max_freq + k:
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)
        