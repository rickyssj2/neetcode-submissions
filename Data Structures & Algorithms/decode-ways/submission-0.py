class Solution:
    def numDecodings(self, s: str) -> int:
        # 231023720932720237429347204623
        #         ^ 
        #         i
        # 23102372 -> x == dp[i - 1]
        # 23102372|0 -> No ways, assuming I take zero individually
        # 2310237|20 -> dp[i - 2] ways

        # if s[0] is not valid: return 0

        # dp[-1] = 0
        # dp[0] = 1

        # dp[i] -> Number of ways to decode uptil i

        # dp[i] = dp[i - 1] if s[i] is valid + dp[i - 2] if s[i-1:i] is valid
        n = len(s)
        dp = [0] * (n + 1)
        if s[0] == '0': return 0

        dp[-1] = 1
        dp[0] = 1

        for i in range(1, n):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2]
        # print(dp)
        return dp[n-1]