class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pair = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        pair_close = {v : k for k, v in pair.items()}
        for c in s:
            if c in pair:
                seen.append(c)
            elif seen and pair_close[c] == seen[-1]:
                seen.pop()
            else:
                return False
        if len(seen) > 0:
            return False
        return True
