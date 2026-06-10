class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for ch in word:
            ptr = ptr.children.setdefault(ch, TrieNode())
        ptr.is_word = True

    def search(self, word: str) -> bool: # 
        def _search(ptr, word):
            if not ptr:
                return False
            if not word:
                return ptr.is_word

            ans = False
            if word[0] == '.':
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    ans |= _search(ptr.children.get(ch, None), word[1:])
                    if ans:
                        return True
                return False

            elif word[0] not in ptr.children:
                return False
            print(word)
            return _search(ptr.children[word[0]], word[1:])
        
        return _search(self.root, word)
        
