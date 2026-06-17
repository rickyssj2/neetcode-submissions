class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        def backtrack(t, comb):
            if t == 0:
                # duplicates
                key = tuple(sorted(comb))
                ans.add(key)
                return
            if t < 0:
                return
            
            for num in nums:
                comb.append(num)
                backtrack(t - num, comb)
                comb.pop()

        backtrack(target, [])
        
        return [list(e) for e in ans]