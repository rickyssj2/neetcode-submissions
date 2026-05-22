class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            total = nums[l] + nums[r]

            if total == target:
                return [l + 1, r + 1]
            elif target > total:
                l += 1
            else:
                r -= 1

        # invariant = moving right, total stays the same or reduces
        # invariant2 = moving left, total stays the same or increases
        