import operator
import PIL
import PIL.Image

INPUT = "/tmp/sec.png"
OUTPUT = "secret.data"

image = PIL.Image.open(INPUT)

tbl = [
    (0, 0, 0),
    (0x7f, 0, 0),
    (0, 0x7f, 0),
    (0, 0, 0x7f),
    (0, 0x7f, 0x7f),
    (0x7f, 0, 0x7f),
    (0x7f, 0x7f, 0),
    (0x55, 0x55, 0x55),

    (0xaa, 0xaa, 0xaa),
    (0xff, 0, 0),
    (0, 0xff, 0),
    (0, 0, 0xff),
    (0, 0xff, 0xff),
    (0xff, 0, 0xff),
    (0xff, 0xff, 0),
    (0xff, 0xff, 0xff),
]

def decode_from_pixel(pixel):
    r,g,b = pixel
    # 下面就是传说中的最小二乘法
    def fdiff(tb):
        rr, rg, rb = tb
        return (r - rr)**2 + (g - rg)**2 + (b - rb)**2
    diffs = list(map(fdiff, tbl))
    # min_index 来源 https://stackoverflow.com/a/2474238
    min_index, min_value = min(enumerate(diffs), key=operator.itemgetter(1))
    return min_index # 这就是编码的值了

four_bit_list = []

# decode image
for y in range(1024):
    for x in range(1024):
        r,g,b,_ = image.getpixel((x, y))
        four_bit_list.append(decode_from_pixel((r,g,b)))

four_bit_pair = [tuple(four_bit_list[n:n+2]) for n in range(0, len(four_bit_list), 2)]

def compose_bit(pair):
    low, high = pair
    return low + (high << 4)

bitstream_in_integer = map(compose_bit, four_bit_pair)

the_data = bytearray(bitstream_in_integer)

with open(OUTPUT, 'wb') as f:
    f.write(the_data)
