from heapq import heapify, heappop

class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parent = list(range(n))
    
    def union(self, u, v):
        if self.connected(u, v): return False

        pu, pv = self.find(u), self.find(v)
        self.parent[pv] = pu
    
    def find(self, u):
        if self.parent[u] == u: return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum Spanning Tree (MST)
        # N, N - 1 edges in a tree

        # Prims, Kruskals

        # Greedy + UF
        n = len(points)
        pq = []
        uf = UnionFind(n)
        for i, (xi, yi) in enumerate(points):
            for j, (xj, yj) in enumerate(points):
                if i == j: continue

                md = abs(xi - xj) + abs(yi - yj)
                pq.append((md, i, j)) # heappush()
        
        heapify(pq) # O(n)

        cost = 0
        edges = 0
        while pq:
            md, u, v = heappop(pq)
            if uf.connected(u, v): continue

            uf.union(u, v)
            cost += md
            edges += 1
            if edges == n - 1: break
        return cost