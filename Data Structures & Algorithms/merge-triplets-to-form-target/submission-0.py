class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cand = [0, 0, 0]

        for t in triplets:
            a, b, c = t
            x, y, z = target
            if a <= x and b <= y and c <= z:
                cand = [max(cand[i], t[i]) for i in range(3)]
                if cand == target: return True
        return False