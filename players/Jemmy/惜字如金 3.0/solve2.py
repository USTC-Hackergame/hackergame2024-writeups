import requests
import json
from z3 import *


# def crc(input: bytes) -> int:
#     poly, poly_degree = 'AaaaaaAaaaAAaaaaAAAAaaaAAAaAaAAAAaAAAaaAaaAaaAaaA', 48
#     assert len(poly) == poly_degree + 1 and poly[0] == poly[poly_degree] == 'A'
#     flip = sum(['a', 'A'].index(poly[i + 1]) << i for i in range(poly_degree))
#     digest = (1 << poly_degree) - 1
#     for b in input:
#         digest = digest ^ b
#         for _ in range(8):
#             digest = (digest >> 1) ^ (flip if digest & 1 == 1 else 0)
#     return digest ^ (1 << poly_degree) - 1


# def hash(input: bytes) -> bytes:
#     digest = crc(input)
#     u2, u1, u0 = 0xCb4EcdfD0A9F, 0xa9dec1C1b7A3, 0x60c4B0aAB4Bf
#     assert (u2, u1, u0) == (223539323800223, 186774198532003, 106397893833919)
#     digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)
#     return digest


def crc_unknown(input: bytes, flip: BitVec) -> int:
    poly_degree = 48
    digest = BitVecVal((1 << poly_degree) - 1, 48)
    for b in input:
        digest = digest ^ b
        for _ in range(8):
            digest = LShR(digest, 1) ^ If(digest & 1 == 1, flip, 0)
    return digest ^ (1 << poly_degree) - 1


def hash_unknown(input: bytes, flip: BitVec) -> bytes:
    digest = crc_unknown(input, flip)
    u2, u1, u0 = 0xdbeEaed4cF43, 0xFDFECeBdeeD9, 0xB7E85A4E5Dcd
    assert (u2, u1, u0) == (241818181881667, 279270832074457, 202208575380941)
    digest = digest * (digest * u2 + u1) + u0
    return digest


def gethash(content_list):
    filecontent = '\n'.join(content_list).encode()

    proxies = {"http": "http://127.0.0.1:8888/",
               "https": "http://127.0.0.1:8888/", }
    base_url = 'http://202.38.93.141:19975/'

    result = requests.post(base_url + '/answer_b.py',
                           proxies=proxies, data=filecontent).text
    result = json.loads(result)['wrong_hints']

    ret = []
    for v in result.values():
        b = bytes.fromhex(v[16:-1])
        v = int.from_bytes(b, 'little')
        ret.append(v)
    return ret


def to_str(flip: int) -> str:
    res = 'B'
    for i in range(48):
        res += 'B' if flip & 1 else 'b'
        flip >>= 1
    return res


solver = Solver()
flip_bv = BitVec('flip', 48)

content_list = ['A' * i for i in range(97)]
hash_list = gethash(content_list)

for (c, h) in zip(content_list, hash_list):
    filehash = hash_unknown(c.encode(), flip_bv)
    solver.add(filehash == h)

res = solver.check()
if res != sat:
    print('unsat')
    exit()
model = solver.model()
flip = model[flip_bv].as_long()
print(hex(flip))
print(to_str(flip))
