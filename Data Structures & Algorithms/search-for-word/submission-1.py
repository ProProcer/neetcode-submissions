class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(coord):
            if len(visited) == len(word):
                return True
            for c in ["UP", "DOWN", "LEFT", "RIGHT"]:
                if c == "UP":
                    new_coord = (coord[0] -1, coord[1])
                    if new_coord[0] < 0:
                        continue
                elif c == "DOWN":
                    new_coord = (coord[0] +1, coord[1])
                    if new_coord[0] >= len(board):
                        continue
                elif c == "LEFT":
                    new_coord = (coord[0], coord[1] -1)
                    if new_coord[1] < 0:
                        continue
                elif c == "RIGHT":
                    new_coord = (coord[0], coord[1] + 1)
                    if new_coord[1] >= len(board[0]):
                        continue
                if board[new_coord[0]][new_coord[1]] != word[len(visited)]:
                    continue

                if new_coord in visited:
                    continue
                visited.add(new_coord)
                if backtrack(new_coord):
                    return True
                visited.remove(new_coord)
                
                    
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    if backtrack((i, j)):
                        return True

        return False
