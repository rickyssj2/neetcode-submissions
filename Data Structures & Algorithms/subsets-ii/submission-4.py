class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        nums.sort()

        def backtrack(i, subset):
            if i == n:
                subsets.append(subset.copy())
                return
            
            # Subsets with atleast one nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # Subsets with no nums[i]
            j = i
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1
            
            backtrack(j + 1, subset)
        
        backtrack(0, [])

        return subsets