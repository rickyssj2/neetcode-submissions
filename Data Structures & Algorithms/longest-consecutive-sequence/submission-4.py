class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5] longest = 4

        # Always start from a num, when num - 1 not in numset
        numset = set(nums)
        longest = 0
        for num in numset:
            if num - 1 not in numset:
                l = 0
                while num in numset:
                    l += 1
                    num += 1
                longest = max(longest, l)
        return longest

