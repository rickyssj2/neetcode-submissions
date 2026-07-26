class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            tmp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    tmp[j] = 1 + dp[j + 1]
                else:
                    tmp[j] = max(tmp[j + 1], dp[j])
            dp = tmp
        return dp[0]