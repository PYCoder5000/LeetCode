class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decoded_dict = {' ': ' '}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decoded_m = ""
        for letter in key:
            if alphabet == "":
                break
            if letter not in decoded_dict.keys():
                decoded_dict[letter] = alphabet[0]
                alphabet = alphabet[1:]
        for letter in message:
            decoded_m += decoded_dict[letter]
        return decoded_m