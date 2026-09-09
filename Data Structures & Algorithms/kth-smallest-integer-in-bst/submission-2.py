# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        stack.append(root)
        while stack:
            node = stack[-1]
            if node.left:
                stack.append(node.left)
                node.left = None
            else:
                k -= 1
                val = stack.pop().val
                if k == 0:
                    return val
                if node.right:
                    stack.append(node.right)
            