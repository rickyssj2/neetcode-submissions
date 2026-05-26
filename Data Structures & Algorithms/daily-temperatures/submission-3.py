class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i] <- (j - i) such that temperatures[j] > temperatures[i]
        n = len(temperatures)
        result = [0] * n
        stack = [] # ALWAYS ascending top -> bottom

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
                
            result[i] = stack[-1][1] - i if stack else 0

            stack.append((temperatures[i], i))
        return result