"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_mapping = {}
        root = Node(node.val)
        queue = deque()
        queue.append((root, node))
        clone_mapping[node] = root
        while queue:
            curr_clone, curr_ori = queue.popleft()
            print(curr_clone.neighbors, curr_ori.neighbors)
            for n in curr_ori.neighbors:
                if n not in clone_mapping:
                    clone_mapping[n] = Node(n.val)
                    queue.append((clone_mapping[n], n))
                curr_clone.neighbors.append(clone_mapping[n])
        return root
