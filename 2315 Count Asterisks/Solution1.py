class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        allow_count = True
        for l in s:
            if l == "|":
                allow_count = not allow_count
            if allow_count and l == "*":
                count += 1
        return count