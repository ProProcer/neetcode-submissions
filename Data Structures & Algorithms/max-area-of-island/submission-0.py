class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            area = 1
            queue = deque()
            queue.append((row, col))
            grid[row][col] = -1
            while queue:
                curr_row, curr_col = queue.popleft()
                for row_delta, col_delta in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_row = curr_row + row_delta
                    new_col = curr_col + col_delta
                    if not(0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
                        continue
                    if grid[new_row][new_col] != 1:
                        continue
                    area += 1
                    grid[new_row][new_col] = -1
                    queue.append((new_row, new_col))
            return area
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(bfs(i, j), max_area)
        return max_area