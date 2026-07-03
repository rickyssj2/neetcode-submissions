from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sn = sum(nums)

        if target + sn > 2 * sn: return 0

        dp = [[False] * (2 * sn + 1) for _ in range(n + 1)]
        dp[n][target + sn] = True

        for i in range(n - 1, -1, -1):
            for t in range(2 * sn + 1):
                plus = dp[i + 1][t + nums[i]] if t + nums[i] < (2 * sn + 1) else 0
                minus = dp[i + 1][t - nums[i]] if 0 <= t - nums[i] else 0
                dp[i][t] = plus + minus

        return dp[0][sn]

