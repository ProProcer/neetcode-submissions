class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for word in wordDict:
            if s.startswith(word):
                dp[len(word) - 1] = True
        for i in range(1, len(s)):
            if not dp[i-1]:
                continue
            for word in wordDict:
                if len(word) > len(s)- i:
                    continue
                if dp[i + len(word) - 1] == False:
                    dp[i + len(word) - 1] = s[i : ].startswith(word)
        return dp[-1]
