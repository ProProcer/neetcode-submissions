class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list  =  []
        for x in s:
            if x.isalnum():
                s_list.append(x)
          

        return s_list[0 : (len(s_list)) //2] == s_list[-1 : len(s_list) - (len(s_list)) //2 - 1 : -1]