class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in ("x", "0"):
                    continue
                island += 1
                queue = deque()
                queue.append((i, j))
                grid[i][j] = "x"
                while queue:

                    r, c = queue.popleft()
                    
                    
                    for rd, cd in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if not(0 <= r + rd < len(grid)):
                            continue
                        if not(0 <= c + cd < len(grid[0])):
                            continue
                        if grid[r + rd][c + cd] == "1":
                            grid[r + rd][c + cd] = "x"
                            queue.append((r + rd, c + cd))
                


        return island