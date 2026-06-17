class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # [9,2,4,6,1,5,2,2,2,2,2,2,2]
        # [12222224569]
        candidates.sort()

        def backtrack(i, t, comb):
            if t == 0:
                ans.append(comb.copy())
                return
            if t < 0 or i == len(candidates): return

            # while j + 1 < len(candidates) and candidates[j] == candidates[j+1]:
            #     j += 1
            # backtrack(j + 1, t, comb)

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                comb.append(candidates[j])
                backtrack(j + 1, t - candidates[j], comb)
                comb.pop()

        
        backtrack(0, target, [])

        return ans