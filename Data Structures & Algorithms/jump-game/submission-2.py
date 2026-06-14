class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_i = 0

        for i, num in enumerate(nums):
            if max_i >= i:
                max_i = max(max_i, i + num)
            if max_i >= (n - 1): return True
        
        return False