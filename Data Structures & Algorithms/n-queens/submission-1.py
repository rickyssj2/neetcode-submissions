class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols ,cols, pDia, nDia = [], set(), set(), set()
        def backtrack(r: int, board: List[str]) -> None:
            if len(board) == n: return sols.append(board.copy())
            for c in range(n):
                if c in cols or r + c in pDia or r - c in nDia: continue
                cols.add(c), pDia.add(r + c), nDia.add(r - c), board.append('.' * c + 'Q' + '.' * (n - c - 1))
                backtrack(r + 1, board)
                cols.remove(c), pDia.remove(r + c), nDia.remove(r - c), board.pop()
        backtrack(0, [])
        return sols