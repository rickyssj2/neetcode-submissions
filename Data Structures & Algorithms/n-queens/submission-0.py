class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [".Q..","...Q","Q...","..Q."]
        # Each row should have exactly one queen (all(row.count(Q) == 1 for row in board))
        # Each col should have exactly one queen (all(col.count(Q) == 1 for col in board))
        # Each dia should have at most one queen 
        sols = []
        cols, pDia, nDia = set(), set(), set()
    
        def backtrack(r: int, board: List[str]) -> None:
            if len(board) == n:
                return sols.append(board.copy())

            for c in range(n):
                cell = (r, c)
                # Column conflict, pDia conflict, nDia conflict:
                if c in cols or r + c in pDia or r - c in nDia:
                    continue
                
                cols.add(c), pDia.add(r + c), nDia.add(r - c)
                rr = ['.'] * n
                rr[c] = 'Q'
                board.append("".join(rr))
                backtrack(r + 1, board)
                cols.remove(c), pDia.remove(r + c), nDia.remove(r - c)
                board.pop()


        backtrack(0, [])
        return sols