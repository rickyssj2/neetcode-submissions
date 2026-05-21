class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row validation
        
        for row in board:
            nset, num_count = set(), 0
            for num in row:
                if num != '.':
                    nset.add(num)
                    num_count += 1
            if num_count != len(nset):
                return False

        # Col validation
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        # Box validation
        boxes_set = [set() for _ in range(9)]
        boxes_num_count = [0] * 9

        for r in range(9):
            for c in range(9):
                box_r = r // 3
                box_c = c // 3
                box_i = box_r * 3 + box_c
                if board[r][c] != '.':
                    boxes_set[box_i].add(board[r][c])
                    boxes_num_count[box_i] += 1

        for i in range(9):
            box_set = boxes_set[i]
            num_count = boxes_num_count[i]
            if len(box_set) != num_count:
                return False
        
        return True
