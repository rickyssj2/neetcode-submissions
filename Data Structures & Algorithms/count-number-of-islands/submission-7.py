class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])
        DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c):
            grid[r][c] = '-1'

            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    dfs(nr, nc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands