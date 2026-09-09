# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkEqual(self, root, subRoot):
        stack = [(root, subRoot)]   

        while stack:
            x, y = stack.pop()
            if not x or not y:
                if x != y:
                    return False
                continue
            elif x.val != y.val:
                return False
            stack.append((x.left, y.left))
            stack.append((x.right, y.right))
        return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if self.checkEqual(node, subRoot):
                return True
            queue.extend([node.left, node.right])
        return False