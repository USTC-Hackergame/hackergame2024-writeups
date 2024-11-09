from pyVNC.Client import Client
from pyVNC.constants import *
from threading import Thread
from time import sleep
from PIL import Image
from hashlib import sha256


def monitor(screen):
    updated = screen.updated
    while True:
        if updated != screen.updated:
            updated = screen.updated
            screen.save_stable('stable.bmp')


def decode(s):
    assert len(s) == 8
    b = [0, 0, 0]

    b[0] = (s[0] << 5) | (s[1] << 2) | ((s[2] & 0b110) >> 1)
    b[1] = ((s[2] & 0b1) << 7) | (s[3] << 4) | (
        s[4] << 1) | ((s[5] & 0b100) >> 2)
    b[2] = ((s[5] & 0b11) << 6) | (s[6] << 3) | (s[7])

    return bytes(b)


def decode_screen(px):
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

    if px[L + 6, U + 9] == (0, 0, 0):
        return None

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
    for c in range(96):
        rr, gg, bb = px[L + c * W + 6, U + H_COUNT * H + 9]
        checksum.append(color[(rr << 16) | (gg << 8) | bb])
    checksum = b''.join([decode(checksum[i:i+8])
                        for i in range(0, len(checksum), 8)])
    index = int.from_bytes(checksum[-4:], 'big')
    checksum = checksum[:-4]

    assert sha256(data).digest() == checksum

    return data, index


if __name__ == '__main__':
    vnc = Client(host='127.0.0.1', password=None, port=12345, depth=32)
    vnc.start()
    print('Connected')

    screen = vnc.screen._screen
    monitor_thread = Thread(target=monitor, args=(screen,))
    monitor_thread.start()

    input('Press Enter to open terminal')
    vnc.send_press(K_LCTRL)
    vnc.send_press(K_LALT)
    vnc.send_press('t')
    sleep(0.02)
    vnc.send_release(K_LCTRL)
    vnc.send_release(K_LALT)
    vnc.send_release('t')
    sleep(1)
    vnc.send_key(K_F11, duration=0.1)
    sleep(2)

    vnc.send_line('vim help.py')
    sleep(1)

    vnc.send_line(':set paste')
    vnc.send_key('i')

    with open('help.py', 'r') as f:
        for c in f.read():
            vnc.send_key(c if c != '\n' else K_RETURN)

    input('Press Enter to save and exit')
    vnc.send_key(K_ESCAPE)
    vnc.send_line(':wq')

    sleep(1)
    vnc.send_line('python3 help.py')

    with open('secret', 'wb') as f:
        round = -1
        while True:
            round += 1
            print(f'Round {round}')
            sleep(1)
            while True:
                try:
                    img = Image.fromarray(screen.get_stable(), 'RGB')
                    d, index = decode_screen(img.load())
                    if index != round:
                        print('Index mismatch', index, round)
                        continue
                except Exception as e:
                    print('Error in round', round, e)
                    continue
                break
            if d is None:
                break
            f.write(d)
            vnc.send_key(K_RETURN)
    
    vnc.send_key(K_RETURN)
    vnc.send_line('ls -la /secret')
    sleep(1)
    vnc.send_line('sha256sum /secret')

    input('Press Enter to exit')
    exit(0)

