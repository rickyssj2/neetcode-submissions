class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            tmp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                tmp[j] = dp[j] + tmp[j + 1]
            dp = tmp

        return dp[0]