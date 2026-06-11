class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
        self.refs = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        ptr = self.root
        for ch in word:
            ptr.refs += 1
            ptr = ptr.children.setdefault(ch, TrieNode())
        ptr.refs += 1
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

        def checkadd(i, j, ptr, pptr, visited) -> int:
            matches = 0
            if ptr.is_word:
                matches += 1
                ptr.is_word = False
                ans.add(ptr.word)

            for di, dj in DELTAS:
                ni, nj = i + di, j + dj
                if valid(ni, nj, visited, ptr):
                    visited.add((ni, nj))
                    ch = board[ni][nj]
                    matches += checkadd(ni, nj, ptr.children[ch], ptr, visited)
                    visited.remove((ni, nj))
            ptr.refs -= matches
            if ptr.refs == 0:
                del pptr.children[board[i][j]] # del "n".children["d"]
            return matches

        ans = set()
        for i in range(m):
            for j in range(n):
                ch, ptr = board[i][j], trie.root
                if ch in ptr.children:
                    matches = checkadd(i, j, ptr.children[ch], ptr, set({(i, j)}))
                    ptr.refs -= matches
                if not trie.root.children:
                    return list(ans)
        return list(ans)