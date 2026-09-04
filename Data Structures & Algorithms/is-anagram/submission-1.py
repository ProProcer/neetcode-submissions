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
        
        set_s = set(key + '^%$(*)' + str(val) for key, val in s_dict.items())
        
        for key, val in t_dict.items():
            if key + '^%$(*)' + str(val) not in set_s:
                return False
        return True