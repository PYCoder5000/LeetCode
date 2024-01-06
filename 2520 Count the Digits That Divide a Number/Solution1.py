class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while temp != 0:
            if num % (temp % 10) == 0:
                count += 1
            temp //= 10
        return count