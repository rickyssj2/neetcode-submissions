from math import inf

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford Algo
        dist = [inf] * n
        dist[src] = 0

        for i in range(k + 1):
            nDist = dist.copy()
            for node, nei, w in flights:
                nDist[nei] = min(nDist[nei], dist[node] + w)
            dist = nDist

        ans = dist[dst]
        return ans if ans != inf else -1
