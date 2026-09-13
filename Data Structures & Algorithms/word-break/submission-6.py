class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)
        
        def helper(start_idx):
            if start_idx == len(s):
                return True
            if cache[start_idx] is not None:
                return cache[start_idx]
            
            for c in wordDict:
                if not s.startswith(c, start_idx):
                    continue
                if helper(start_idx + len(c)):
                    cache[start_idx] = True
                    return True
                
            cache[start_idx] = False
            return False
        return helper(0)