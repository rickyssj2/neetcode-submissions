class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([])
        DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        fresh_cnt = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        t = 0
        while q:
            r, c, t = q.popleft()

            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 # mark as visited
                    fresh_cnt -= 1
                    q.append((nr, nc, t + 1))

        return t if fresh_cnt == 0 else -1

