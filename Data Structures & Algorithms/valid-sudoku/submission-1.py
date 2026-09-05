class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in sets:
                        # print(i, j, 'row')
                        return False
                    else:
                        sets.add(board[i][j])
            sets.clear()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in sets:
                        # print(j, i, 'col')
                        return False
                    else:
                        sets.add(board[j][i])
            sets.clear()
            
            for j in range(9):
                box_i = i // 3 * 3 + j // 3
                box_j = i % 3 * 3 + j % 3
                if board[box_i][box_j] != '.':
                    # print(board[box_i][box_j])
                    if board[box_i][box_j] in sets:
                        # print(box_i, box_j, 'box')
                        return False
                    else:
                        # print(sets)
                        sets.add(board[box_i][box_j])
            sets.clear()
            
            
        return True