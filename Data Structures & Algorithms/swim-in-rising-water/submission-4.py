class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, u, v):
        if self.connected(u, v): return False

        pu, pv = self.find(u), self.find(v)
        self.parent[pv] = pu
        return True
    
    def find(self, u):
        if self.parent[u] == u: return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        imap = defaultdict(tuple)

        for i in range(n):
            for j in range(n):
                imap[grid[i][j]] = (i, j)

        def index(i, j):
            return i * n + j

        def update(t):
            i, j = imap[t]
            for di, dj in deltas:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= t:
                    uf.union(index(i, j), index(ni, nj))
                    
        for t in range(n * n * n):
            if t not in imap: continue
            update(t)

            if uf.connected(index(0, 0), index(n - 1, n - 1)):
                return t
            
        return -1