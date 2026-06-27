from functools import cache

class Solution:
    # @cache
    def climbStairs(self, n: int) -> int:
        # Recursion
        # if n <= 1: return 1

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # Tabulation
        if n < 2: return 1

        a, b = 1, 1
        c = -1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return c