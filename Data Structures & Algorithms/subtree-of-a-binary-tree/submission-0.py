# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root == subRoot
        equal_sub = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if equal_sub:
            return True
        equal = True
        stack = [(root, subRoot)]
        while stack:
            node_r, node_s = stack.pop()
            if not node_r or not node_s:
                if node_r != node_s:
                    equal = False
                    break
                continue
            elif node_r.val != node_s.val:
                equal = False
                break
            stack.append((node_r.left, node_s.left))
            stack.append((node_r.right, node_s.right))
        return equal