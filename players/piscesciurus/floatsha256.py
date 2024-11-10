import sys
from functools import cache

class F:
    """一个常量或运算得到的浮点数。"""

    n = 0  # 类上计数器，实例上编号
    k = False  # 是否为常量
    v = float("nan")  # 常量值；变量值为调试用

    def __init__(self) -> None:
        self.n = F.n
        print(self.n, file=sys.stderr)
        F.n += 1

    def __repr__(self) -> str:
        return f"F{self.n}[={self.v}]"

    sub_cache: dict[tuple[int, int], "F"] = {}
    def __sub__(self, other: "F") -> "F":
        if self.k and other.k:
            return K(self.v - other.v)
        if (self.n, other.n) not in self.sub_cache:
            f = F()
            f.v = self.v - other.v
            print(self.n, other.n)
            self.sub_cache[self.n, other.n] = f
        return self.sub_cache[self.n, other.n]

    def __neg__(self) -> "F":
        return K(0) - self

    inv_cache: dict[int, "F"] = {}
    def __invert__(self) -> "F":
        if self.n not in self.inv_cache:
            assert self.v in (0, 1)
            inv = K(1) - self
            self.inv_cache[self.n] = inv
            self.inv_cache[inv.n] = self
        return self.inv_cache[self.n]

    def __add__(self, other: "F") -> "F":
        return self - -other

    def __and__(self, other: "F") -> "F":
        assert self.v in (0, 1) and other.v in (0, 1)
        return self + other - K(1) - K(1 << 53) - K(-(1 << 53))

    def __xor__(self, other: "F") -> "F":
        assert self.v in (0, 1) and other.v in (0, 1)
        s = self + other
        return s - (s - K(0.5) - K(1 << 53) - K(-(1 << 53)))

    @staticmethod
    def adc(a: "F", b: "F", c: "F") -> tuple["F", "F"]:  # 带进位加法，返回(低位, 进位)
        assert a.v in (0, 1) and b.v in (0, 1) and c.v in (0, 1)
        s = a + b + c
        carry2 = s - K(0.5) - K(1 << 53) - K(-(1 << 53))
        carry = carry2 - K(1) - K(1 << 53) - K(-(1 << 53))
        return s - carry2, carry

@cache
def K(x: float) -> F:
    f = F()
    f.v = float(x)
    f.k = True
    print(x)
    return f

def V(x: float) -> F:
    f = F()
    f.v = float(x)
    return f

class B:
    """由多个0/1浮点数构成的字，字长不定。"""

    def __init__(self, bits: list[F]) -> None:
        assert bits
        self.bits = bits

    def __repr__(self) -> str:
        v = int("".join(str(int(c.v)) for c in reversed(self.bits)), 2)
        return f"B:{len(self.bits)}[={v:#x}]"

    @staticmethod
    def from_byte(byte: F) -> "B":
        bits: list[F] = []
        a = 63.5
        b = 128.0
        c = float(1 << 60)
        for _ in range(7):
            bits.append(byte - K(a) - K(c) - K(-c))
            byte -= bits[-1]
            a /= 2
            b /= 2
            c /= 2
            bits = [x - K(b) - K(c) - K(-c) for x in bits]
        bits.append(byte)
        bits.reverse()
        return B(bits)

    @staticmethod
    def K(x: int, bit_length: int) -> "B":
        return B([K(x >> i & 1) for i in range(bit_length)])

    def to_f(self) -> F:
        y = self.bits[-1]
        for x in self.bits[-2::-1]:
            y += y
            y += x
        return y

    def __and__(self, other: "B") -> "B":
        assert len(self.bits) == len(other.bits)
        return B([a & b for a, b in zip(self.bits, other.bits)])

    def __xor__(self, other: "B") -> "B":
        assert len(self.bits) == len(other.bits)
        return B([a ^ b for a, b in zip(self.bits, other.bits)])

    def __invert__(self) -> "B":
        return B([~x for x in self.bits])

    def __add__(self, other: "B") -> "B":
        assert len(self.bits) == len(other.bits)
        bits = [self.bits[0] ^ other.bits[0]]
        carry = self.bits[0] & other.bits[0]
        for i in range(1, len(self.bits)):
            y, carry = F.adc(self.bits[i], other.bits[i], carry)
            bits.append(y)
        return B(bits)

    def ror(self, x: int) -> "B":
        assert 0 < x < len(self.bits)
        return B(self.bits[x:] + self.bits[:x])

    def __rshift__(self, x: int) -> "B":
        assert 0 < x < len(self.bits)
        return B(self.bits[x:] + [K(0)] * x)


def generate_hash() -> None:
    # 改编自https://github.com/keanemind/Python-SHA-256
    TABLE = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ]

    def sigma0(x: B) -> B:
        return B.ror(x, 7) ^ B.ror(x, 18) ^ (x >> 3)

    def sigma1(x: B) -> B:
        return B.ror(x, 17) ^ B.ror(x, 19) ^ (x >> 10)

    def capsigma0(x: B) -> B:
        return B.ror(x, 2) ^ B.ror(x, 13) ^ B.ror(x, 22)

    def capsigma1(x: B) -> B:
        return B.ror(x, 6) ^ B.ror(x, 11) ^ B.ror(x, 25)

    def ch(x: B, y: B, z: B) -> B:
        return (x & y) ^ (~x & z)

    def maj(x: B, y: B, z: B) -> B:
        return (x & y) ^ (x & z) ^ (y & z)

    message_block = [V(x) for x in b"qwertyuiopasdfghjklzxcvbnm678901"]
    message_block = [B.from_byte(x) for x in message_block]
    message_block.extend(B.K(x, 8) for x in b"\x80" + b"\0" * 29 + b"\1\0")
    assert len(message_block) == 64

    # Setting Initial Hash Value
    h0 = B.K(0x6a09e667, 32)
    h1 = B.K(0xbb67ae85, 32)
    h2 = B.K(0x3c6ef372, 32)
    h3 = B.K(0xa54ff53a, 32)
    h5 = B.K(0x9b05688c, 32)
    h4 = B.K(0x510e527f, 32)
    h6 = B.K(0x1f83d9ab, 32)
    h7 = B.K(0x5be0cd19, 32)

    # Prepare message schedule
    message_schedule = [
        B(
            message_block[t + 3].bits
            + message_block[t + 2].bits
            + message_block[t + 1].bits
            + message_block[t].bits
        )
        for t in range(0, 64, 4)
    ]
    for t in range(16, 64):
        term1 = sigma1(message_schedule[t - 2])
        term2 = message_schedule[t - 7]
        term3 = sigma0(message_schedule[t - 15])
        term4 = message_schedule[t - 16]
        message_schedule.append(term1 + term2 + term3 + term4)
    assert len(message_schedule) == 64

    # Initialize working variables
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    # Iterate for t=0 to 63
    for t in range(64):
        t1 = h + capsigma1(e) + ch(e, f, g) + B.K(TABLE[t], 32) + message_schedule[t]
        t2 = capsigma0(a) + maj(a, b, c)

        h = g
        g = f
        f = e
        e = d + t1
        d = c
        c = b
        b = a
        a = t1 + t2

    # Compute intermediate hash value
    h0 = h0 + a
    h1 = h1 + b
    h2 = h2 + c
    h3 = h3 + d
    h4 = h4 + e
    h5 = h5 + f
    h6 = h6 + g
    h7 = h7 + h

    output = [
        B(b).to_f()
        for h in (h0, h1, h2, h3, h4, h5, h6, h7)
        for b in (h.bits[24:], h.bits[16:24], h.bits[8:16], h.bits[:8])
    ]
    output = [o - K(0) for o in output]
    print("EOF")


generate_hash()
