from math import inf
from heapq import heappush, heappop
# from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algo
        # Bellman-Ford Algo

        dist = [inf] * (n + 1)
        dist[k] = 0
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        for i in range(n - 1):
            for node in range(1, n + 1):
                for nei, w in adj[node]:
                    dist[nei] = min(dist[nei], dist[node] + w)

        ans = max(dist[1:])
        return ans if ans != inf else -1
