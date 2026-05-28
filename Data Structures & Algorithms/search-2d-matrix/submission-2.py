class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m*n + log(m*n))
        m, n = len(matrix), len(matrix[0])

        l, r = 0 , m * n - 1

        while l <= r:
            mid = (l + r) // 2 # 5
            rr, cc = divmod(mid, n)

            if matrix[rr][cc] == target:
                return True
            elif matrix[rr][cc] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False