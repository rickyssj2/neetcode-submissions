class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque([])
        DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            r, c, d = q.popleft()

            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    if grid[nr][nc] >= d + 1:
                        grid[nr][nc] = min(grid[nr][nc], d + 1)
                        q.append((nr, nc, d + 1))
        