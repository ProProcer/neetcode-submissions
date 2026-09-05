class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxs = [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val)
                if (1 << val) & rows[i] != 0:
                    return False
                if (1 << val) & cols[j] != 0:
                    return False
                if (1 << val) & boxs[i // 3 * 3 + j // 3] != 0:
                    return False
                rows[i] |= (1 << val)
                cols[j] |= (1 << val)
                boxs[i // 3 * 3 + j // 3] |= (1 << val)
        return True
