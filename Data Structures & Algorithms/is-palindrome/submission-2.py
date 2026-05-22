class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        print(cleaned)
        l, r = 0, len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True