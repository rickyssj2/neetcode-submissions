class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Interval DP
        # Smaller sub-problems have smaller interval sizes
        # We solve smallest interval to largest interval

        # dp[i][j] => (i .... j) max points to burst balloons from i....j
        # i < k < j
        # dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] for all k)
        # dp[i][i] = nums[i]
        nums = [1] + nums + [1]
        
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]
        
        for l in range(2, n + 1): # Not an index, but a physical size
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n - 1]
