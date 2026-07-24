class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Build p2 and character mapping q
        q = {}
        n, m = len(s), len(p)
        p2 = ""
        i = 0
        while i < m:
            if i + 1 < m and p[i + 1] == '*':
                p2 += '*'
                q[len(p2) - 1] = p[i]
                i += 1
            else:
                p2 += p[i]
            i += 1
        
        o = len(p2)

        dp = [[False] * (o + 1) for _ in range(n + 1)]
        dp[n][o] = True

        # Outer loop MUST start from n so empty string matching (i = n) is handled!
        for i in range(n, -1, -1):
            for j in range(o - 1, -1, -1):
                if p2[j] == '*':
                    # Option 1: Match 0 instances (always valid to skip the '*')
                    dp[i][j] |= dp[i][j + 1]
                    
                    # Option 2: Match 1+ instances (only valid if i < n and chars match)
                    if i < n and (s[i] == q[j] or q[j] == '.'):
                        dp[i][j] |= dp[i + 1][j] or dp[i + 1][j + 1]

                elif i < n:
                    if p2[j] == '.' or p2[j] == s[i]:
                        dp[i][j] |= dp[i + 1][j + 1]

        return dp[0][0]