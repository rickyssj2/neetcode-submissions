class Solution:
    def ed(self, a, b):
        n, ed = len(a), 0

        for i in range(n):
            ed += (a[i] != b[i])
        
        return ed

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        if endWord not in wordList: return 0

        wordList += [beginWord]
        w = len(wordList)

        for i in range(w - 1):
            a = wordList[i]
            for j in range(i + 1, w):
                b = wordList[j]
                if self.ed(a, b) == 1:
                    adj[a].append(b)
                    adj[b].append(a)
        
        q = deque([(beginWord, 0)])
        visited = set({beginWord})

        while q:
            node, d = q.popleft()

            for nei in adj[node]:
                if nei == endWord:
                    return d + 2
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, d + 1))

        return 0

