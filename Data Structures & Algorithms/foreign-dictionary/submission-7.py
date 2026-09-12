class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        recorded_edge = set()
        indegree = {}
        for i in range(0, len(words)):
            for ch in words[i]:
                adj[ch] = []
                indegree[ch] = 0
        for i in range(1, len(words)):
            
            safe = False
            for left, right in zip(words[i - 1], words[i]):
                if left == right:
                    continue
                if (left, right) in recorded_edge:
                    safe = True
                    break
                recorded_edge.add((left, right))
  
                adj[left].append(right)
                indegree[right] += 1
                safe = True
                break
            
            if len(words[i-1]) > len(words[i]) and not safe:
    
                return ""
        
        queue = deque()
        visited = set()
        sequence = []
        
        for i, count in indegree.items():
            if count == 0:
                queue.append(i)
                visited.add(i)
                sequence.append(i)
        # print(indegree)
        while queue:
            curr = queue.popleft()
            for child in adj[curr]:
                if child in visited:
                    continue
                indegree[child] -= 1
                if indegree[child] != 0:
                    continue
                queue.append(child)
                visited.add(child)
                sequence.append(child)
        if len(visited) != len(indegree):

            # print(sequence)
            return ""
        return "".join(sequence)
        
        

