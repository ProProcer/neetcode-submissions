class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def run_queue(queue):
            visited = set(queue)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < len(heights) and 0 <= nc < len(heights[0])):
                        continue
                    if (nr, nc) in visited:
                        continue
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            return visited
        queue_pacific = deque()
        queue_atlantic = deque()
        for i in range(len(heights)):
            queue_pacific.append((i, 0))
            queue_atlantic.append((i, len(heights[0]) -1))
        for j in range(len(heights[0])):
            queue_pacific.append((0, j))
            queue_atlantic.append((len(heights) -1, j))
        return list(run_queue(queue_pacific) & run_queue(queue_atlantic))
