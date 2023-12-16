class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        total = (n * (n + 1))/2
        for val in range(1, n + 1):
            if val % m != 0:
                num1 += val
        return int(2 * num1 - total)