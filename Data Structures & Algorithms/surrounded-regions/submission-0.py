class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque([])
        DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        safe_set = set()

        for r in [0, m - 1]:
            for c in range(n):
                if board[r][c] == "O":
                    q.append((r, c))
                    safe_set.add((r, c))
        
        for r in range(1, m - 1):
            for c in [0, n - 1]:
                if board[r][c] == "O":
                    q.append((r, c))
                    safe_set.add((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and (nr, nc) not in safe_set:
                    safe_set.add((nr, nc))
                    q.append((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in safe_set:
                    board[r][c] = 'X'
        

            
