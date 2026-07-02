from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # patience sort
        sub = []

        for i, num in enumerate(nums):
            idx = bisect_left(sub, num)

            if idx == len(sub): sub.append(num)
            else: sub[idx] = num
        
        return len(sub)