class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n  = len(nums)
        subsets = []
        def backtrack(i, comb):
            if i == n:
                subsets.append(comb.copy())
                return
            
            backtrack(i + 1, comb)
            comb.append(nums[i])
            j = i + 1
            while j < n and nums[j] == nums[j - 1]:
                comb.append(nums[j])
                j += 1
            backtrack(j, comb)
            for _ in range(j - i):
                comb.pop()
        
        backtrack(0, [])
        return subsets