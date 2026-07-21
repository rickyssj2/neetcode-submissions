class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # [[1, 1, 2],
        #  [3, 2, 1],
        #  [4, 3, 2]]
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]
        DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        explored = [[False] * n for _ in range(m)]

        def bfs(r, c):
            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    if not explored[nr][nc]:
                        explored[nr][nc] = True
                        bfs(nr, nc)
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
        
        for i in range(m):
            for j in range(n):
                if explored[i][j]: continue

                explored[i][j] = True
                bfs(i, j)

        return max([max(row) for row in dp])

        