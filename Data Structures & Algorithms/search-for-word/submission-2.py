class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def search(r, c, word, visited) -> bool:
            if board[r][c] != word[0]:
                return False
            
            visited.add((r, c))
            nword = word[1:]
            if not nword:
                return True
            
            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    if search(nr, nc, nword, visited):
                        return True

            visited.remove((r, c))
            return False


        for r in range(n):
            for c in range(m):
                if search(r, c, word, set()):
                    return True
        
        return False