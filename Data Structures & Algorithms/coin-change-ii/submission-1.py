from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort() # Maybe not needed
        n = len(coins)

        @cache
        def backtrack(i, bal):
            if bal < 0 or i == n:
                return 0
            if bal == 0:
                return 1
            
            subcnt = 0
            # take the ith coin
            subcnt += backtrack(i, bal - coins[i])

            # skip, move to next coin
            subcnt += backtrack(i + 1, bal)

            return subcnt

        
        return backtrack(0, amount)

        