class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = list(range(n))
        self.size = [1] * (n)
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv: return 

        if self.size[pu] >= self.size[pv]:
            self.p[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.p[pu] = pv
            self.size[pv] += self.size[pu]
    
    def find(self, u):
        if self.p[u] == u: return u
        self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        ans = None

        for u, v in edges:
            if uf.connected(u - 1, v - 1): ans = [u, v]
            else: uf.union(u - 1, v - 1)
        
        return ans