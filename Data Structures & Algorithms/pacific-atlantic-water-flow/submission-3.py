class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        q = deque([])
        DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        pacific_set = set()
        atlantic_set = set()

        # Pacific
        r = 0
        for c in range(n):
            q.append((r, c))
            pacific_set.add((r, c))
        
        c = 0
        for r in range(m):
            q.append((r, c))
            pacific_set.add((r, c))
                
        while q:
            r, c = q.popleft()

            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in pacific_set:
                    pacific_set.add((nr, nc))
                    q.append((nr, nc))
        # Atlantic
        r = m - 1
        for c in range(n):
            q.append((r, c))
            atlantic_set.add((r, c))
        
        c = n - 1
        for r in range(m):
            q.append((r, c))
            atlantic_set.add((r, c))
                
        while q:
            r, c = q.popleft()

            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in atlantic_set:
                    atlantic_set.add((nr, nc))
                    q.append((nr, nc))

        return list(pacific_set & atlantic_set)