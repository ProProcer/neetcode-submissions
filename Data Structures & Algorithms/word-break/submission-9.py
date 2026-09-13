class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                if s.startswith(word, i):
                    dp[i + len(word)] = True
        return dp[-1]