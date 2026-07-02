from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] -> can i break the substring [i...n - 1]

        # dp[i] = dp[i + k] if [i... i + k - 1] in dict for k in range(0, n - i)


        # return dp[0] # [0....n-1]

        n = len(s)
        wordset = set(wordDict)

        @cache
        def dp(i):
            if i == n: return True

            for k in range(1, n - i + 1):
                if s[i : i + k] in wordset:
                    if dp(i + k):
                        return True
            
            return False

        return dp(0)