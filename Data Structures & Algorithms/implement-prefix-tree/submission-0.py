class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root

        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root

        for ch in word:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        
        for ch in prefix:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        
        return True
        
        