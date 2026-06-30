class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = 0
        for i in range(n):
            dp[i][i] = True
            ans += 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if i + 1 > j - 1: dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else: 
                    dp[i][j] = False
                
                if dp[i][j]:
                    ans += 1

        return ans