class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        n = len(candidates)

        def backtrack(i, cand, total):
            if total == target:
                combinations.append(cand.copy())
                return

            if i == n or total > target:
                return
            
            # Pick
            cand.append(candidates[i])
            backtrack(i + 1, cand, total + candidates[i])
            cand.pop()

            # Skip
            j = i + 1
            while j < n and candidates[j] == candidates[j - 1]:
                j += 1
            backtrack(j, cand, total)
        
        backtrack(0, [], 0)
        return combinations
