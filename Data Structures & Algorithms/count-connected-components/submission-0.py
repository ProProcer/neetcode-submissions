class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        not_visited = set(range(n))
        queue = deque() 
        n = 0      
        while not_visited:
            n += 1
            queue.append(not_visited.pop())
            while queue:
                curr = queue.popleft()
                for child in adj[curr]:
                    if child in not_visited:
                        not_visited.remove(child)
                        queue.append(child)
        return n