class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        queue = deque()
        queue.append((0, -1))
        visited = [False] * n
        visited[0] = True
        while queue:
            curr, prev = queue.popleft()

            for child in adj[curr]:
                if visited[child]:
                    if child == prev:
                        continue
                    else:
                        return False
                queue.append((child, curr))
                visited[child] = True
        return sum(visited) == n