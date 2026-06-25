class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        # connectivity
        # run a bfs/dfs from any starting, if you visit all nodes -> connected

        q = deque([0])
        visited = [False] * n
        visited[0] = True
        
        while q:
            node = q.popleft()

            for nei in adj[node]:
                if not visited[nei]: 
                    visited[nei] = True
                    q.append(nei)
        
        return all(visited)
