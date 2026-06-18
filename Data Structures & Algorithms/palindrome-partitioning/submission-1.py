class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = [] # [['a', 'a', 'b'], ["aa", "b"]]
        n = len(s)

        def isPalin(a):
            return a == a[::-1]

        def backtrack(i, partitions, cand): # 0, [], "" -> 1, [], "a" -> 2, ["aa"], "" -> 3
            if i == n:
                if isPalin(cand):
                    if cand: partitions.append(cand)
                    ans.append(partitions.copy())
                return

            cand += s[i] # "b"
            # Partition
            if cand and isPalin(cand):
                partitions.append(cand) # ['aa', "b"]
                backtrack(i + 1, partitions, "")
                partitions.pop()
            
            # No partition
            if i < n - 1:
                backtrack(i + 1, partitions, cand)

        backtrack(0, [], "")

        return ans