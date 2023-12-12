class Trie:

    def __init__(self):
        self.tree = set()
        self.prefix = set()

    def insert(self, word: str) -> None:
        if word not in self.tree:
            self.tree.add(word)
            for i in range(len(word)-1,0,-1):
                if word[:i] in self.prefix:
                    break
                self.prefix.add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.tree
            

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.tree or prefix in self.prefix


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)