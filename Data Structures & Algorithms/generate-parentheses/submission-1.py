class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []

        def backtrack(open, avail, paren):
            if len(paren) == 2*n:
                parens.append(paren)
                return
            
            if open:
                backtrack(open - 1, avail, paren + ')')

            if avail:
                backtrack(open + 1, avail - 1, paren + '(')
        
        backtrack(0, n, "")

        return parens
            