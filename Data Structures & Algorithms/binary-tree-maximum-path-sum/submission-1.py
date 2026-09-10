# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = -float('inf')
        def helper(root):
            if root.left:
                max_left = helper(root.left)
            else:
                max_left = None
            if root.right:
                max_right = helper(root.right)
            else:
                max_right = None
            if max_left and max_right:
                if root.val >= 0:
                    self.maxsum = max(self.maxsum, max_left + root.val, max_right + root.val, max_left + max_right + root.val, root.val)
                else:
                    self.maxsum = max(self.maxsum, max_left, max_right, max_left + max_right + root.val, root.val)
                return max(max_left + root.val, max_right + root.val, root.val, root.val)
            elif max_left:
                self.maxsum = max(self.maxsum, root.val + max_left, max_left, root.val)
                return max(max_left + root.val, root.val)
            elif max_right:
                self.maxsum = max(self.maxsum,root.val + max_right, max_right, root.val)
                return max(max_right + root.val, root.val)
            else:
                self.maxsum = max(self.maxsum, root.val)
                return root.val
        helper(root)
        return self.maxsum