class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1: return False

        # nums.sort()
        target = sum(nums) // 2
        # dp(0) = True
        def dp(t, candidates):
            if t < 0: return False
            if t == 0: return True

            for i, c in enumerate(candidates):
                if dp(t - c, candidates[i + 1:]): return True
            
            return False


        return dp(target, nums) # Can I select a subset with sum == target