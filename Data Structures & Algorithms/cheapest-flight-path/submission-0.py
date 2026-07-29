from math import inf

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford Algo
        dist = [inf] * n
        dist[src] = 0
        adj = defaultdict(list)

        for u, v, w in flights:
            adj[u].append((v, w))

        for i in range(k + 1):
            nDist = dist.copy()
            for node in range(n):
                for nei, w in adj[node]:
                    nDist[nei] = min(nDist[nei], dist[node] + w)
            dist = nDist

        ans = dist[dst]
        return ans if ans != inf else -1
        # dist = [inf] * n
        # dist[src] = 0

        # # At most k stops = at most k + 1 edges/flights
        # for _ in range(k + 1):
        #     temp = dist.copy()
        #     for u, v, w in flights:
        #         if dist[u] != inf and dist[u] + w < temp[v]:
        #             temp[v] = dist[u] + w
        #     dist = temp

        # return dist[dst] if dist[dst] != inf else -1