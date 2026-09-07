from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        count_dict = defaultdict(int)
        l = 0
        max_freq = 0
        for r in range(len(s)):
            count_dict[s[r]] += 1
            max_freq = max(max_freq, count_dict[s[r]])
            while r - l + 1 - max_freq > k:
                count_dict[s[l]] -= 1
                l += 1
            max_length = max(r - l + 1, max_length)
        return max_length
                
