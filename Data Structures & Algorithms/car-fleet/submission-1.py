class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        idx = list(range(n))
        idx.sort(key=lambda x: position[x])
        time = [(target - position[i]) / speed[i] for i in idx]
        numfleets = 0
        stack = [] # ALWAYS ascending top -> bottom

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] < time[i]:
                stack.pop()
                
            numfleets += not stack

            stack.append((time[i], i))
        return numfleets