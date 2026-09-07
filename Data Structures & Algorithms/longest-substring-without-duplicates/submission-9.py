class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            r += 1
            longest = max(longest, r - l)
        return longest