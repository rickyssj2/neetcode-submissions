class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # h -> e -> r -> n -> f

        # h -> e
        # f -> e
        # e -> n
        # h -> n
        # hfe, fhe

        # "" <- all alpha, cyclic === invalid

        # It should have a valid toposort
        def diff(w1, w2):
            n = min(len(w1), len(w2))
            d = []
            for i in range(n):
                if w1[i] != w2[i]:
                    return w1[i], w2[i]
            return False

        n = len(words)
        adj = defaultdict(list)

        for w1, w2 in pairwise(words): # TODO
            if not diff(w1, w2):
                if len(w1) > len(w2): return ""
            else:
                a, b = diff(w1, w2) # a -> b
                adj[a].append(b)
            
        for word in words:
            for ch in word: adj[ch]

        def idx(a):
            return ord(a) - ord('a')
        
        # Topo sort (Kahn's Algo)
        indeg = [0] * 26
        for neis in adj.values():
            for nei in neis:
                indeg[idx(nei)] += 1
        
        q = deque([letter for letter in adj.keys() if indeg[idx(letter)] == 0]) # Main kya daal sakta hun

        topo = ""
        while q:
            letter = q.popleft()
            topo += letter
            for nei in adj[letter]:
                indeg[idx(nei)] -= 1
                if indeg[idx(nei)] == 0: q.append(nei)
        
        return topo if len(topo) == len(adj) else ""
