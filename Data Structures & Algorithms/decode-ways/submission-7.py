class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        prev_prev = 1
        prev = 1
        
        for i in range(1, len(s)):
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
