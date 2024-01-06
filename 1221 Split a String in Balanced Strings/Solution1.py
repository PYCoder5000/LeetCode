class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        sub = 0
        for d in s:
            if d == "R":
                r += 1
            else:
                r -= 1
            if r == 0:
                sub += 1
        return sub
        