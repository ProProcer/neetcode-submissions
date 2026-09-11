class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word: str):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.insert(w)

        rows, cols = len(board), len(board[0])
        matched_words = []

        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            curr_node = parent_node.children.get(char)
            if not curr_node:
                return

            if curr_node.word:
                matched_words.append(curr_node.word)
                curr_node.word = None  # Prevent duplicate insertions

            # In-place marking avoids hash set allocation
            board[r][c] = '#'
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
            board[r][c] = char

            # Optimization: prune leaf nodes during unwinding
            if not curr_node.children:
                parent_node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return matched_words