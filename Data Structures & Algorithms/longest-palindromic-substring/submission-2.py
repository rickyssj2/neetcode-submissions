class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        ans = s[0]
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
                    ans = s[i:j + 1]
        return ans

