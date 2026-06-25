class Solution:
    def findOrder(self, numc: int, prereq: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indeg = [0] * numc

        for u, v in prereq:
            adj[v].append(u)
            indeg[u] += 1
        
        q = deque([i for i in range(numc) if indeg[i] == 0])

        # O(V + E) 
        order = []

        while q:
            c = q.popleft() # Popping means I am taking this course now
            order.append(c)

            for nei in adj[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0: q.append(nei)
        
        return order if len(order) == numc else []