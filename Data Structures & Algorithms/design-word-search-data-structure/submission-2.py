class TriesNode:
    def __init__(self):
        self.children = {}
        self.exist = False
class WordDictionary:

    def __init__(self):
        self.root = TriesNode()
        
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TriesNode()
            curr = curr.children[c]
        curr.exist = True
    def search(self, word: str) -> bool:
        
        def is_exist(idx, root):
            curr = root
            for i in range(idx, len(word)):
        
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        exist = is_exist(i + 1, child)
                        if exist:
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            if curr.exist:
                return True
            else:
                return False
        return is_exist(0, self.root)
