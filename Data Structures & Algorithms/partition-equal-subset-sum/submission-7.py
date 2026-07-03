class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1: return False

        # nums.sort()
        target = sum(nums) // 2
        # dp(0) = True
        # def dp(t, candidates):
        #     if t < 0: return False
        #     if t == 0: return True

        #     for i, c in enumerate(candidates):
        #         if dp(t - c, candidates[i + 1:]): return True
            
        #     return False


        # return dp(target, nums) # Can I select a subset with sum == target

        # dp[i][j] Can I make target == i with nums[j:]

        n = len(nums)
        dp = [[False] * (n + 1) for _ in range(target + 1)]
        dp[0] = [True] * (n + 1)


        for t in range(target + 1):
            for i in range(n - 1, -1, -1):
                # Skip
                dp[t][i] |= dp[t][i + 1]

                # Take, if nums[i] <= t
                if t - nums[i] >= 0:
                    dp[t][i] |= dp[t - nums[i]][i + 1]

        return dp[target][0]