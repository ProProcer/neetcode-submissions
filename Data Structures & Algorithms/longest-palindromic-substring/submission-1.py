class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_left = 0
        max_right = 0
        for i in range(1, len(s) - 1):
            left = i -1
            right = i + 1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                if right - left + 1 > max_right - max_left + 1:
                    max_right = right
                    max_left = left
                left -= 1
                right += 1
        for i in range(0, len(s) - 1):
            left = i
            right = i + 1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                if right - left + 1 > max_right - max_left + 1:
                    max_right = right
                    max_left = left
                left -= 1
                right += 1
        return s[max_left : max_right + 1]
