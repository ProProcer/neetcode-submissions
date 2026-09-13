class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            left = i
            right = i
            while right < len(s) and left >= 0 and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        for i in range(0, len(s) - 1):
            left = i
            right = i + 1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count