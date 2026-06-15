from math import inf 

class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i]: miminum jumps required to reach index i (0 ≤ i < n)
        # dp[i] = min [ 1 + dp[j] (j + nums[j] ≥ i) (0 ≤ j < i) ]
        q = deque([0])
        visited = set({0})
        dist = 0
        n = len(nums)
        if n <= 1: return 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for nei in range(node + 1, min(n, node + nums[node] + 1)):
                    if nei == (n - 1):
                        return dist + 1
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            dist += 1
        return -1