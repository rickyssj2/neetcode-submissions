class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        # [9,2,4,6,1,5,2,2,2,2,2,2,2]
        # [1222222]
        candidates.sort()
        def backtrack(i, t, comb):
            if t == 0:
                ans.add(tuple(comb))
                return
            if t < 0 or i == len(candidates): return
            
            j = i
            comb.append(candidates[j])
            backtrack(j + 1, t - candidates[j], comb)
            comb.pop()

            while j + 1 < len(candidates) and candidates[j] == candidates[j+1]:
                j += 1
            backtrack(j + 1, t, comb)

        
        backtrack(0, target, [])

        return [list(e) for e in ans]