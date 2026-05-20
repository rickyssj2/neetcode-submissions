class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in numset:
            if num - 1 not in numset:
                cur = 0
                while num in numset:
                    cur += 1
                    num += 1
                ans = max(ans, cur)
        return ans
