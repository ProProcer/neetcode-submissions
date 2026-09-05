class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            box_set = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        # print(i, j, 'row')
                        return False
                    else:
                        row_set.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        # print(j, i, 'col')
                        return False
                    else:
                        col_set.add(board[j][i])
                box_i = i // 3 * 3 + j // 3
                box_j = i % 3 * 3 + j % 3
                if board[box_i][box_j] != '.':
                    if board[box_i][box_j] in box_set:
                        # print(box_i, box_j, 'box')
                        return False
                    else:
                        box_set.add(board[box_i][box_j])
        return True