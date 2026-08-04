class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euler Tour/ Path of a DG
        # Hierholzer's Algo (backtracking)

        # 1) out == in for all vertices
        # 2) start: out - in == 1 AND end: in - out == 1
        # start should be JFK (1 or 2)

        adj = defaultdict(list)
        out = defaultdict(int)

        for start, end in tickets:
            adj[start].append(end)
            out[start] += 1
        
        for k in adj.keys():
            adj[k].sort(reverse=True)
        
        et = []

        def dfs(node):
            if not out[node]:
                return et.append(node)
            
            while out[node]:
                out[node] -= 1
                nxt = out[node]
                dfs(adj[node][nxt])
            
            et.append(node)

        dfs("JFK")

        return et[::-1]