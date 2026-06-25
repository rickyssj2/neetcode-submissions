class Solution:
    def canFinish(self, numc: int, prereq: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0] * numc

        for u, v in prereq:
            adj[v].append(u)
            indeg[u] += 1
        
        q = deque([i for i in range(numc) if indeg[i] == 0])

        while q:
            c = q.popleft()

            for nei in adj[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0: q.append(nei)
        
        return all(indeg[i] == 0 for i in range(numc))