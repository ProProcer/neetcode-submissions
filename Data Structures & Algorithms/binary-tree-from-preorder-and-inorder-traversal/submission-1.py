# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        order_map = {v : i for i , v in enumerate(inorder)}

        self.i = 0
        def helper(left, right):
            if left == right:
                self.i += 1
                return TreeNode(preorder[self.i -1])
            if left > right:
                return None
            
            val = preorder[self.i]
            node = TreeNode(val)
            self.i += 1
            node.left = helper(left, order_map[val] - 1)
            node.right = helper(order_map[val] + 1, right)
            return node                
        return helper(0, len(preorder) -1)
        