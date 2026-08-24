class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1 = sorted(s1)
        l = 0
        win = len(s1)
        for l in range(len(s2)-len(s1)+1):
            print(f"l={l} and r = {l+win}")
            print(s2[l:l+win])
            if sorted(s2[l:l+win]) == s1:
                return True
        return False
        