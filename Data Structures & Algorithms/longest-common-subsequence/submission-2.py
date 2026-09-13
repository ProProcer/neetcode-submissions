class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev_row = [0] * (len(text1) + 1)
        curr_row = [0] * (len(text1) + 1)
        for i in range(len(text2)):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i]:
                    curr_row[j] = prev_row[j - 1] + 1
                else:
                    curr_row[j] = max(curr_row[j - 1], prev_row[j])
            prev_row = curr_row
            curr_row = [0] * (len(text1) + 1)

        return prev_row[-1]