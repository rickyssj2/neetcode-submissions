class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        n = len(nums)

        for i in range(n):
            cprod = 1
            for j in range(i, n):
                cprod *= nums[j]
                ans = max(ans, cprod)
        
        return ans