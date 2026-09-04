from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        
        return s_dict == t_dict