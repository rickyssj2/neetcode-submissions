class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t[-1].isdigit():
                stack.append(int(t))
            else:
                r, l, res = stack.pop(), stack.pop(), 0
                
                if t == '+':
                    res = r + l
                if t == '-':
                    res = l - r
                if t == '*':
                    res = l * r
                if t == '/':
                    res = int(l / r)
                
                stack.append(res)
        return stack.pop()