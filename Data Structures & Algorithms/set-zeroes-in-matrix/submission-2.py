class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        topleft = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        topleft = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if i == 0:
                    contain_zero = topleft == 0
                else:
                    contain_zero = matrix[i][0] == 0
                contain_zero = contain_zero or matrix[0][j] == 0
                if contain_zero:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if topleft == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                