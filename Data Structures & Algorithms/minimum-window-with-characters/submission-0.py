from collections import defaultdict
import copy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        best_l = 0
        best_r = len(s)
        count_dict = defaultdict(int)
        valid_dict = defaultdict(int)
        for x in t:
            valid_dict[x] += 1
        residual_dict = copy.deepcopy(valid_dict)
        for r in range(len(s)):
            if s[r] in valid_dict:
                count_dict[s[r]] += 1
                residual_dict[s[r]] -= 1
                if residual_dict[s[r]] <= 0:
                    del residual_dict[s[r]]
            while len(residual_dict) == 0:
                if r - l + 1 < best_r - best_l + 1:
                    best_l, best_r = l, r
                if s[l] in valid_dict:
                    count_dict[s[l]] -= 1
                    if count_dict[s[l]] < valid_dict[s[l]]:
                        residual_dict[s[l]] += 1
                l += 1
        if best_r == len(s):
            return ""
        return s[best_l : best_r + 1]