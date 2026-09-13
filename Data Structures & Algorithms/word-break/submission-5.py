class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)
        
        def helper(start_idx):
            if start_idx == len(s):
                return True
            if cache[start_idx] is not None:
                return cache[start_idx]
            res = False
            for c in wordDict:
                if not s.startswith(c, start_idx):
                    continue
                res = helper(start_idx + len(c))
                if res:
                    break
            cache[start_idx] = res
            return res
        return helper(0)