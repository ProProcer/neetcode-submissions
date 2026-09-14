class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) // 2 ):
            for j in range(i, len(matrix) - i - 1):
                top = matrix[i][j]
                right = matrix[j][len(matrix) - 1 - i]
                bot = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
                left = matrix[len(matrix) - j - 1][i]
                matrix[i][j] = left
                matrix[j][len(matrix) - 1 - i] = top
                matrix[len(matrix) - i - 1][len(matrix) - j - 1] = right
                matrix[len(matrix) - j - 1][i] = bot
        