class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        order_map = {val: i for i, val in enumerate(inorder)}
        self.i = 0

        def helper(left: int, right: int) -> TreeNode | None:
            # 1. Base case: empty subtree
            if left > right:
                return None

            # 2. Consume root immediately (preorder property)
            val = preorder[self.i]
            self.i += 1
            node = TreeNode(val)

            # 3. Partition inorder index space
            mid = order_map[val]

            # 4. Construct left before right (matches preorder consumption)
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            return node

        return helper(0, len(inorder) - 1)