from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sn = sum(nums)

        if abs(target) > sn:
            return 0

        width = 2 * sn + 1
        dp = [[0] * width for _ in range(n + 1)]
        dp[n][target + sn] = 1

        for i in range(n - 1, -1, -1):
            for t in range(width):
                plus = dp[i + 1][t + nums[i]] if t + nums[i] < width else 0
                minus = dp[i + 1][t - nums[i]] if t - nums[i] >= 0 else 0
                dp[i][t] = plus + minus

        return dp[0][sn]  # t=0 unshifted corresponds to index sn

