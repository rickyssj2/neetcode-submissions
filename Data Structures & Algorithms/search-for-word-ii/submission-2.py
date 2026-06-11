class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        ptr = self.root
        for ch in word:
            ptr = ptr.children.setdefault(ch, TrieNode())
        ptr.is_word = True
        ptr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        trie = Trie()
        for word in words:
            trie.insert(word)

        def valid(ni, nj, visited, ptr) -> bool:
            return 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and board[ni][nj] in ptr.children

        def checkadd(i, j, ptr, visited):
            if ptr.is_word:
                ans.add(ptr.word)

            for di, dj in DELTAS:
                ni, nj = i + di, j + dj
                if valid(ni, nj, visited, ptr):
                    visited.add((ni, nj))
                    ch = board[ni][nj]
                    checkadd(ni, nj, ptr.children[ch], visited)
                    visited.remove((ni, nj))
        
        ans = set()
        for i in range(m):
            for j in range(n):
                ch, ptr = board[i][j], trie.root
                if ch in ptr.children:
                    checkadd(i, j, ptr.children[ch], set({(i, j)}))
        return list(ans)