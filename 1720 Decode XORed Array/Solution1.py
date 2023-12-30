class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for encode in encoded:
            decoded.append(decoded[-1] ^ encode)
        return decoded