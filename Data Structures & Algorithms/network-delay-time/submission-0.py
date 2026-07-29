from math import inf
from heapq import heappush, heappop
# from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [inf] * (n + 1) # [0, 1 ....., n]
        pq = [(0, k)] # (dist, node)
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        while pq:
            d, node = heappop(pq)
            if d >= dist[node]: continue

            dist[node] = d

            for nei, w in adj[node]:
                nd = d + w
                if nd < dist[nei]:
                    heappush(pq, (nd, nei))
        
        ans = max(dist[1:])
        return ans if ans != inf else -1