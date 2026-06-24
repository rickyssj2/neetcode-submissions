class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c): # returns the area of the un-walked sub-island starting from this node
            grid[r][c] = -1
            nArea = 0
            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    nArea += dfs(nr, nc)
            return 1 + nArea

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area