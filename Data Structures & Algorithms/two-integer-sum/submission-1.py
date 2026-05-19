class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            if num in hmap:
                return [hmap[num], i]
            hmap[target - num] = i