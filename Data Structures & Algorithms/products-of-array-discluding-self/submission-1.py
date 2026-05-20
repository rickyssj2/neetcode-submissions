class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf, prod = [1] * (n + 1), [1] * (n + 1), [0] * n
        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
            suf[n - i - 1] = nums[n - i] * suf[n - i]
        for i in range(n):
            prod[i] = pre[i] * suf[i]
        return prod