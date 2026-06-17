class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(mask, perm):
            if not nums:
                ans.append(perm.copy())
                return
            if mask == 2**n - 1:
                ans.append(perm.copy())
                return
            
            for k, num in enumerate(nums):
                if mask & (1 << k):
                    continue
                
                perm.append(num)
                backtrack(mask | (1 << k), perm)
                perm.pop()

        backtrack(0, [])

        return ans