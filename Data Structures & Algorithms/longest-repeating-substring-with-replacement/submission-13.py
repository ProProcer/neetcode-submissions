from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "ABCDZZZ"
        # k = 3
        max_length = 0
        count_dict = defaultdict(int)
        l = 0
        for r in range(len(s)):
            print(l, r)
            count_dict[s[r]] += 1
            _, curr_root = max((v, k) for k, v in count_dict.items())
            while r - l + 1 - count_dict[curr_root] > k:
                count_dict[s[l]] -= 1
                l += 1
                _, curr_root = max((v, k) for k, v in count_dict.items())
            curr_length = r - l + 1
            max_length = max(curr_length, max_length)
        return max_length
                
