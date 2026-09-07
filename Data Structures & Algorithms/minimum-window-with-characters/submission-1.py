from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        target = Counter(t)
        window = {}
        
        have = 0
        need = len(target)
        
        min_len = float("inf")
        best_l, best_r = 0, 0
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            # Did this incoming character just satisfy its required quota?
            if char in target and window[char] == target[char]:
                have += 1
            
            # Contract from the left while the window remains fully valid
            while have == need:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    best_l, best_r = l, r
                
                left_char = s[l]
                # If removing left_char violates target quota, drop 'have'
                if left_char in target and window[left_char] == target[left_char]:
                    have -= 1
                
                window[left_char] -= 1
                l += 1
                
        return s[best_l : best_r + 1] if min_len != float("inf") else ""