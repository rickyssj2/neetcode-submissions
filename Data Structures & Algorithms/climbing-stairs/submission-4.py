from functools import cache

class Solution:
    # @cache
    def climbStairs(self, n: int) -> int:
        # Recursion
        # if n <= 1: return 1

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # Tabulation
        if n < 2: return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        print(dp)
        return dp[n]