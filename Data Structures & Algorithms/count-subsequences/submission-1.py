class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] => I have matched j chars of t from the first i elements of s

        # dp[i][j] = sum(dp[i + 1][j + 1] if s[i] == t[j] else 0, dp[i + 1][j])

        # dp[n][m] = 1

        # caaat i = 2
        # cat   j = 1

        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        dp[m] = 1 # i + 1 th row

        for i in range(n - 1, -1, -1):
            tmp = [0] * (m + 1) # ith row
            tmp[m] = 1
            for j in range(m - 1, -1, -1):
                take = dp[j + 1] if s[i] == t[j] else 0
                skip = dp[j]
                tmp[j] = take + skip
            dp = tmp
        return dp[0]