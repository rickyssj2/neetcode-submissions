class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(i, t, comb):
            if t == 0:
                ans.append(comb.copy())
                return
            if t < 0 or i == len(candidates): return

            for j in range(i, len(candidates)):
                if t - candidates[j] < 0: return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                comb.append(candidates[j])
                backtrack(j + 1, t - candidates[j], comb)
                comb.pop()

        
        backtrack(0, target, [])

        return ans