class Solution:
    def checkValidString(self, s: str) -> bool:
        os, ss = [], []

        for i, ch in enumerate(s):
            if ch == '(': os.append(i)
            elif ch == '*': ss.append(i)
            else: 
                if os: os.pop()
                elif ss: ss.pop()
                else: return False

        while os:
            if ss and ss[-1] > os[-1]: ss.pop(), os.pop()
            else: return False

        return True