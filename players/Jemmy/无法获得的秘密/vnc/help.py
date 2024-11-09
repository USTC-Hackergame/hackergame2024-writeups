from hashlib import sha256


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


def print_encoded(encoded_data):
    for c in encoded_data:
        print(f'\033[{str(90 + c)}m\u2588\033[0m', end='', flush=True)

with open('/secret', 'rb') as f:
    data = f.read()

if len(data) % 1425 != 0:
    data += b"\xFF" * (1425 - len(data) % 1425)

for i in range(0, len(data), 1425):
    block = data[i:i+1425]
    index = int.to_bytes(i // 1425, 4, 'big')

    encoded_data = []
    for j in range(0, len(block), 3):
        encoded_data += encode(block[j:j+3])
    print_encoded(encoded_data)

    checksum = sha256(block).digest() + index
    encoded_checksum = []
    for j in range(0, len(checksum), 3):
        encoded_checksum += encode(checksum[j:j+3])
    print_encoded(encoded_checksum)
    input()

print(' ' * 3900)