# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        result = [str(root.val), 'N', 'N']
        queue = deque()
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if node.left:
                result[i] = str(len(result))
                result.extend([str(node.left.val), 'N', 'N'])
                queue.append(node.left)
            if node.right:
                result[i + 1] = str(len(result))
                result.extend([str(node.right.val), 'N', 'N'])
                queue.append(node.right)
            i += 3
        return ','.join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'N':
            return None
        result = data.split(',')
        queue = deque()
        root = TreeNode(result[0])
        queue.append(root)
        i = 0
        while queue:
            node = queue.popleft()
            left_idx = result[i + 1]
            right_idx = result[i + 2]
            if left_idx != 'N':
                node.left = TreeNode(result[int(left_idx)])
                queue.append(node.left)
            if right_idx != 'N':
                node.right = TreeNode(result[int(right_idx)])
                queue.append(node.right)
            i += 3
        return root

