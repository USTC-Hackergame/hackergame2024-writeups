from tqdm import tqdm
from os import urandom

def encode(s: bytes):
    assert len(s) == 3
    b = [None for _ in range(8)]
    b[0] = (s[0] & 0b11100000) >> 5
    b[1] = (s[0] & 0b00011100) >> 2
    b[2] = ((s[0] & 0b00000011) << 1) | ((s[1] & 0b10000000) >> 7)
    b[3] = (s[1] & 0b01110000) >> 4
    b[4] = (s[1] & 0b00001110) >> 1
    b[5] = ((s[1] & 0b00000001) << 2) | ((s[2] & 0b11000000) >> 6)
    b[6] = (s[2] & 0b00111000) >> 3
    b[7] = s[2] & 0b00000111

    return b


def decode(s):
    assert len(s) == 8
    b = [0, 0, 0]

    b[0] = (s[0] << 5) | (s[1] << 2) | ((s[2] & 0b110) >> 1)
    b[1] = ((s[2] & 0b1) << 7) | (s[3] << 4) | (s[4] << 1) | ((s[5] & 0b100) >> 2)
    b[2] = ((s[5] & 0b11) << 6) | (s[6] << 3) | (s[7])

    return bytes(b)

for _ in tqdm(range(1024)):
    data = urandom(3)
    assert decode(encode(data)) == data