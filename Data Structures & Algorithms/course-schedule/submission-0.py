class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = [[] for _ in range(numCourses)]
        towards_me = [0] * numCourses
        for e in prerequisites:
            towards_me[e[0]] += 1
            mapping[e[1]].append(e[0])
        completed = set()
        queue = deque()
        for i, count in enumerate(towards_me):
            if count == 0:
                completed.add(i)
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            for child in mapping[curr]:
                if child in completed:
                    continue
                towards_me[child] -= 1
                if towards_me[child] == 0:
                    completed.add(child)
                    queue.append(child)
        return len(completed) == numCourses

        
