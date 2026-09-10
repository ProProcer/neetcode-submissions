class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word[:-1]:
            if w not in curr:
                curr[w] = [0, {}]
            curr = curr[w][1]
        if word[-1] not in curr:
            curr[word[-1]] = [1, {}]
        else:
            curr[word[-1]][0] += 1
        
            

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word[:-1]:
            if w not in curr:
                return False
            curr = curr[w][1]
        if word[-1] in curr and curr[word[-1]][0] > 0:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w][1]
        return True
        