class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDE'

    def encode(self, str):
        upper_str = str.upper()
        encoded_str = ''
        for letter in upper_str:
            if letter.isalpha():
                index = self.alphabet.index(letter) + self.shift
                modified_idx = index - 26 if index > 26 else index
                encoded_str += self.alphabet[modified_idx]
            else:
                encoded_str += letter
        return encoded_str

    def decode(self, str):
        upper_str = str.upper()
        decoded_str = ''
        for letter in upper_str:
            if letter.isalpha():
                index = self.alphabet.index(letter) - self.shift
                modified_idx = 26 + index if index < 0 else index
                decoded_str += self.alphabet[modified_idx]
            else:
                decoded_str += letter
        return decoded_str

# Improved version
from string import ascii_uppercase as abc

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, s):
        return s.upper().translate(str.maketrans(abc, abc[self.shift:]+abc[:self.shift]))

    def decode(self, s):
        return s.upper().translate(str.maketrans(abc[self.shift:]+abc[:self.shift], abc))

if __name__ == "__main__":
    c = CaesarCipher(5)
    print("Answer:", c.encode('Codewars'))
    print("Answer:", c.decode('BFKKQJX'))

