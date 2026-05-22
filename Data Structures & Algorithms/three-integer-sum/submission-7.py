class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 1, 2]
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n - 2):
            a = nums[i]
            ans = self.twoSum(nums[i + 1:], -a)
            if ans:
                for b, c in ans:
                    result.add((a, b, c))
        
        return list(result)
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        ans = []
        while l < r:
            total = nums[l] + nums[r]

            if total == target:
                ans.append([nums[l], nums[r]])
                l += 1
                r -= 1
            elif target > total:
                l += 1
            else:
                r -= 1
        return ans
            