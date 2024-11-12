import z3

known_hashes = {
    b"\x00" * 80: "5383b8380054",
    # b"00000000000000000000000000000000000000000000000000000000000000000000000000000000": "f956166401e1",
    # b"11111111111111111111111111111111111111111111111111111111111111111111111111111111": "71155dc8fea8",
    # b"22222222222222222222222222222222222222222222222222222222222222222222222222222222": "e50defbbda87",
    # b"33333333333333333333333333333333333333333333333333333333333333333333333333333333": "9d2765269607",
    # b"44444444444444444444444444444444444444444444444444444444444444444444444444444444": "1325b5629659",
    # b"55555555555555555555555555555555555555555555555555555555555555555555555555555555": "0f7dbe5664c1",
    # b"66666666666666666666666666666666666666666666666666666666666666666666666666666666": "338c2c1147d8",
    # b"77777777777777777777777777777777777777777777777777777777777777777777777777777777": "c7d1f2a9f729",
    # b"88888888888888888888888888888888888888888888888888888888888888888888888888888888": "fffae1a0407a",
    # b"99999999999999999999999999999999999999999999999999999999999999999999999999999999": "e314c8ee16b7",
}

solver = z3.Solver()
poly_degree = 48
# flip = z3.Int('flip')
# TypeError: unsupported operand type(s) for >>: 'ArithRef' and 'int'
flip = z3.BitVec("flip", poly_degree)


def crc(s: bytes) -> z3.BitVec:
    # I don't know why but these don't work.
    # solver.add((flip >> 47) == 1)
    # solver.add((flip >> 47) == z3.BitVecVal(1, 48))
    solver.add(flip & (1 << (poly_degree - 1)) == (1 << (poly_degree - 1)))
    # digest = (1 << poly_degree) - 1
    digest = z3.BitVecVal((1 << poly_degree) - 1, poly_degree)
    for b in s:
        digest = digest ^ b
        for _ in range(8):
            digest = (digest >> 1) ^ z3.If((digest & 1) == 1, flip, 0)
    # Operator priority?
    return digest ^ (1 << poly_degree) - 1


def hash(s: bytes) -> z3.BitVec:
    digest = crc(s)
    u2, u1, u0 = 241818181881667, 279270832074457, 202208575380941
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)
    return digest


def main() -> None:
    for text, digest_hex in known_hashes.items():
        digest = int.from_bytes(bytes.fromhex(digest_hex), "little")
        solver.add(hash(text) == digest)
    result = solver.check()
    print(result)
    if result != z3.sat:
        exit(1)
    print(solver.model[flip])


if __name__ == "__main__":
    main()
