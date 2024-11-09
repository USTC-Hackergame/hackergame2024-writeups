from PIL import Image

def decode(s):
    assert len(s) == 8
    b = [0, 0, 0]

    b[0] = (s[0] << 5) | (s[1] << 2) | ((s[2] & 0b110) >> 1)
    b[1] = ((s[2] & 0b1) << 7) | (s[3] << 4) | (s[4] << 1) | ((s[5] & 0b100) >> 2)
    b[2] = ((s[5] & 0b11) << 6) | (s[6] << 3) | (s[7])

    return bytes(b)

with Image.open('stable.bmp') as img:
    px = img.load()
    print(px)
    exit()

    W_COUNT, H_COUNT = 100, 38
    W, H = 10, 19
    L, R, U, D = 1, 23, 26, 1

    color = {
        0x555555: 0,
        0xff5555: 1,
        0x55ff55: 2,
        0xffff55: 3,
        0x5555ff: 4,
        0xff55ff: 5,
        0x55ffff: 6,
        0xffffff: 7,
    }

    for c in range(L-1, L + W_COUNT * W + 2):
        assert px[c, U - 1] == (0, 0, 0), c
        assert px[c, U + (H_COUNT + 1) * H] == (0, 0, 0)

    for r in range(U-1, U + H_COUNT * H + 2):
        assert px[L - 1, r] == (0, 0, 0)
        assert px[L + W_COUNT * W, r] == (0, 0, 0)

    data = []
    for r in range(H_COUNT):
        for c in range(W_COUNT):
            rr, gg, bb = px[L + c * W + 6, U + r * H + 9]
            data.append(color[(rr << 16) | (gg << 8) | bb])
    data = b''.join([decode(data[i:i+8]) for i in range(0, len(data), 8)])

    checksum = []
    for c in range(88):
        rr, gg, bb = px[L + c * W + 6, U + H_COUNT * H + 9]
        checksum.append(color[(rr << 16) | (gg << 8) | bb])
    checksum = b''.join([decode(checksum[i:i+8]) for i in range(0, len(checksum), 8)])[:-1]

    assert sha256(data).digest() == checksum
