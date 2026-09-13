class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev_row = [0] * len(text1)
        curr_row = [0] * len(text1)
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    if j == 0:
                        curr_row[j] = 1
                    else:
                        curr_row[j] = prev_row[j - 1] + 1

                elif j == 0:
                    curr_row[j] = prev_row[j]
                else:
                    curr_row[j] = max(curr_row[j - 1], prev_row[j])
            prev_row = curr_row
            curr_row = [0] * len(text1)

        return prev_row[-1]