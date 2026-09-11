class TriesNode:
    def __init__(self):
        self.children = [None] * 26
        self.exist = False
class WordDictionary:

    def __init__(self):
        self.root = TriesNode()
        
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = TriesNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.exist = True
    def search(self, word: str) -> bool:
        
        def is_exist(idx, root):
            curr = root
            for i in range(idx, len(word)):
            
                if not curr:
                    return False
                c = word[i]
                if c == '.':
                    for child in curr.children:
                        if not child:
                            continue
                        exist = is_exist(i + 1, child)
                        if exist:
                            return True
                    return False
                else:
                    curr = curr.children[ord(c) - ord('a')]

            if curr:
                return curr.exist
            else:
                return False
        return is_exist(0, self.root)
