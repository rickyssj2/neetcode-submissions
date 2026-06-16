class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)

        for b in range(2**n):
            subset = []
            for i in range(n):
                if b & (1 << i):
                    subset.append(nums[i])
            ans.append(subset.copy())
        return ans