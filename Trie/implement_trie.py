class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)