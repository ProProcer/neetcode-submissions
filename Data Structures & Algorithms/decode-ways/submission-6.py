class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        prev_prev = 1
        prev = 1 if s[1] != '0' else 0
        prev = prev + 1 if 10 <= int(s[0 : 2]) <= 26 else prev
        for i in range(2, len(s)):
            temp = prev
            prev = 0
            if 10 <= int(s[i-1:i+1]) <= 26:
                prev = prev_prev
            if s[i] != '0':
                prev += temp
            if not prev:
                return 0
            prev_prev = temp
        return prev
