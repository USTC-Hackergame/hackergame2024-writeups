import requests
import json
from z3 import *
from typing import List
from base64 import b85decode, b85encode
from tqdm import tqdm
from sage.all import matrix, GF, vector
from os import urandom
from Crypto.Util.number import long_to_bytes
from random import choice
from string import printable


def crc(input: bytes) -> int:
    poly, poly_degree = 'CcccCCcCcccCCCCcCCccCCccccCccCcCCCcCCCCCCCccCCCCC', 48
    assert len(poly) == poly_degree + 1 and poly[0] == poly[poly_degree] == 'C'
    flip = sum(['c', 'C'].index(poly[i + 1]) << i for i in range(poly_degree))
    digest = (1 << poly_degree) - 1
    for b in input:
        digest = digest ^ b
        for _ in range(8):
            digest = (digest >> 1) ^ (flip if digest & 1 == 1 else 0)
    return digest ^ (1 << poly_degree) - 1

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def hash(input: bytes) -> bytes:
    digest = crc(input)
    u2, u1, u0 = 0xDfffffffffff, 0xFfffffffffff, 0xFfffffffffff
    assert (u2, u1, u0) == (246290604621823, 281474976710655, 281474976710655)
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)
    return digest.to_bytes(48 // 8, 'little')

def hash_unknown(digest: BitVec) -> bytes:
    u2, u1, u0 = 0xDfffffffffff, 0xFfffffffffff, 0xFfffffffffff
    assert (u2, u1, u0) == (246290604621823, 281474976710655, 281474976710655)
    digest = digest * (digest * u2 + u1) + u0
    return digest

def req(content_list):
    filecontent = b'\n'.join(content_list)

    proxies = {"http": "http://127.0.0.1:8888/",
               "https": "http://127.0.0.1:8888/", }
    base_url = 'http://202.38.93.141:19975/'

    result = requests.post(base_url + '/answer_c.py',
                           proxies=proxies, data=filecontent).text
    result = json.loads(result)['wrong_hints']

    ret = []
    for v in result.values():
        if not v.startswith('Unmatched data ('):
            ret.append(None)
            continue
        index = v[(len('Unmatched data (') + 2):-1]
        ret.append(int(index, 16))
    return ret

def get_crc(hash_val: bytes, length: int) -> List[int]:
    hash_val = int.from_bytes(hash_val, 'little')
    s = Solver()
    crc = BitVec(f'crc', 48)
    s.add(hash_unknown(crc) == hash_val)

    l = []

    while True:
        res = s.check()
        if res != sat:
            break
        model = s.model()
        crc_val = model[crc].as_long()
        l.append(crc_val)
        s.add(crc != crc_val)
    return l

def solve_crc(target: int):
    N = 6 * 8 # Number of vectors
    M = 6 * 8 # Number of bits (Input data length)

    A = matrix(GF(2), M, N)

    for i in range(N):
        data = bytes.fromhex(hex(1<<i)[2:].rjust(M//4, '0')) + b'\x00' * (64 - 6)
        #assert len(data) == 64
        digest = crc(data)
        for j in range (M):
            A[j, i] = 1 if digest & (1<<j) else 0

    B = vector(GF(2), M)

    for j in range(M):
        B[j] = 1 if target & (1<<j) else 0

    result = A.solve_right(B)

    data = 0
    for i in range(N):
        data |= 1<<i if result[i] else 0

    data = long_to_bytes(data, N // 8)
    digest = crc(data + b'\x00' * (64 - 6))

    if digest == target:
        return data

# def get_constant():
#     A = urandom(64)
#     B = urandom(64)
#     C = urandom(64)

#     ca = crc(A)
#     cb = crc(B)
#     cc = crc(C)

#     result = ca^cb^crc(xor(A, B))
#     assert result == cb^cc^crc(xor(B, C))
#     assert result == ca^cc^crc(xor(A, C))

#     return result

def gen_payload(crc_vals: List[int], chars:List[int], known: bytes) -> bytes:
    C = 0x60fb26deb696
    padlen = 64 - 6 - len(known) - 2
    
    payloads = []

    seps = []
    for i in range(32):
        if i != 0x0a and i != 0x0d:
            seps.append(i)
    seps = bytes(seps)

    for val in tqdm(chars):
        delta = None
        while True:
            data = b'\x00' * 6 + bytes([ord(choice(printable)) for _ in range(padlen)]) + bytes([choice(seps), val]) + known
            target = choice(crc_vals)
            delta = solve_crc(target ^ C ^ crc(data))

            if delta is None:
                continue

            data = delta + data[6:]
            assert crc(data) in crc_vals

            if b'\x0a' in data or b'\x0d' in data:
                continue
            else:
                break
        payloads.append(data)

    return payloads


expected_hash = b85decode('answer_c')
assert len(expected_hash) == 6
assert b85encode(expected_hash) == b'answer_c'

expected_crc = get_crc(expected_hash, 64)

length = 64
chars = range(0x20, 0x7f)
known = b'_c6Gc8##buBY?WpXW4axrCOEmSZqM|EX$b1g7#Wi2pfEmUY_EmAOdb3c6'
for pos in range(length - len(known) -  1, 0, -1):
    print(f'pos = {pos}, known = {known}')
    filecontent = gen_payload(expected_crc, chars, known)
    hash_list = req(filecontent)

    found = False
    for w, val in zip(hash_list, chars):
        if w is not None and w < 0x20:
            if not found:
                found = True
                known = bytes([val]) + known
            else:
                print('Found multiple matches')
        elif w is not None and w != val:
            print(f'w = {w}, val = {val}, {chr(val)}')
            exit(0)
    if not found:
        print('No match found')
        exit(0)

# flag{HAV3-Y0u-3ver-Tr1ed-T0-Guess-0ne-0f-The-R0ws?}