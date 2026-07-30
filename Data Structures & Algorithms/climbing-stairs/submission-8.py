from functools import cache

class Solution:
    # @cache
    def climbStairs(self, n: int) -> int:
        # Recursion
        # if n <= 1: return 1

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # Tabulation + SO
        # if n < 2: return 1

        # a, b = 1, 1
        # c = -1
        # for i in range(2, n + 1):
        #     c = a + b
        #     a, b = b, c

        # return c
        def mat_mul(A, B):
            return [
                [A[0][0]*B[0][0] + A[0][1]*B[1][0],  A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0],  A[1][0]*B[0][1] + A[1][1]*B[1][1]],
            ]

        def mat_pow(M, p):
            # Identity matrix
            result = [[1, 0], [0, 1]]
            while p:
                if p & 1:
                    result = mat_mul(result, M)
                M = mat_mul(M, M)
                p >>= 1
            return result

        if n <= 1:
            return 1
        
        M = [[1, 1], [1, 0]]
        return mat_pow(M, n + 1)[0][1]