class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=set(jewels)
        noj = 0
        for stone in stones:
            if stone in jewels:
                noj+=1
        return noj