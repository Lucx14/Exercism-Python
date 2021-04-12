import string
import secrets
from itertools import cycle

ALPHA = string.ascii_lowercase
ENCODE = "encode"
DECODE = "decode"


def generate_secret_key():
    return "".join(secrets.choice(ALPHA) for i in range(100))


class Cipher:
    def __init__(self, key=generate_secret_key()):
        self.key = key

    def encode(self, text):
        return self._run_cipher(text, ENCODE)

    def decode(self, text):
        return self._run_cipher(text, DECODE)

    def _run_cipher(self, text, direction):
        result = []
        for text_char, key_char in zip(text, cycle(self.key)):
            current_position = ALPHA.index(text_char)
            shift_factor = ALPHA.index(key_char)
            new_position = (
                current_position + shift_factor
                if direction == ENCODE
                else current_position - shift_factor
            )
            result.append(ALPHA[new_position % 26])

        return "".join(result)
