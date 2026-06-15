class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        diff = [g - c for g, c in zip(gas, cost)]
        total = sum(diff)
        print(diff)
        maxsum = 0
        cum = 0
        ans = -1
        for i, num in enumerate(diff):
            val = total - cum
            if val >= maxsum:
                maxsum = val
                ans = i
            cum += num
        return ans
        