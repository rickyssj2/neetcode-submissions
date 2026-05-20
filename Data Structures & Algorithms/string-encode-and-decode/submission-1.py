class Solution:

    def encode(self, strs: List[str]) -> str:
        e = []
        for s in strs:
            e.append(f"{len(s)}#{s}")
        return ''.join(e)

    def decode(self, s: str) -> List[str]:
        i, strs = 0, []
        while i < len(s):
            j = s.find('#', i)
            l = int(s[i:j])
            j += 1
            word = s[j: j + l]
            strs.append(word)
            i = j + l
        return strs