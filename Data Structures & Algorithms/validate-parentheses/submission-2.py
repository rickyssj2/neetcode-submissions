class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correct_pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        # {[
        for br in s:
            if br in "({[":
                stack.append(br)
            else:
                if not (stack and stack[-1] == correct_pair[br]):
                    return False
                stack.pop()
        
        return len(stack) == 0