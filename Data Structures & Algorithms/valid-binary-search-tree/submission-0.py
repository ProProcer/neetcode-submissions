# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root.left:
                left_valid, min_left, max_left = dfs(root.left)
            else:
                left_valid, min_left, max_left = True, root.val, root.val
            if root.right:
                right_valid, min_right, max_right = dfs(root.right)
            else:
                right_valid, min_right, max_right = True, root.val, root.val

            
            if not (left_valid and right_valid):
                return False, None, None

            if (max_left if root.left else -float("inf")) < root.val < (min_right if root.right else float("inf")):
                return True, min_left, max_right
            else:
                return False, None, None
        
        res, _, _ = dfs(root)
        return res

                