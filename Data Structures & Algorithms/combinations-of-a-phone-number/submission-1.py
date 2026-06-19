class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        combs = []
        dta = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(i: int, comb: str): # This function decides what options we have for each index i (digit)
            if i == n: # Processed all digits
                if comb: combs.append(comb)
                return

            for ch in dta[digits[i]]:
                backtrack(i + 1, comb + ch)

        backtrack(0, "")
        return combs