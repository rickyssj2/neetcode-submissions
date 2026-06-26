class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # [0....n-1]
        visited = set()
        cc = 0
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited: dfs(nei)
        
        for node in range(n):
            if node not in visited:
                cc += 1
                dfs(node)
        
        return cc