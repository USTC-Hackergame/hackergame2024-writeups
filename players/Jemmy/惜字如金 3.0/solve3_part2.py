import requests
import json
from z3 import *
from typing import List
from base64 import b85decode, b85encode
from tqdm import tqdm


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


def hash(input: bytes) -> bytes:
    digest = crc(input)
    u2, u1, u0 = 0xDfffffffffff, 0xFfffffffffff, 0xFfffffffffff
    assert (u2, u1, u0) == (246290604621823, 281474976710655, 281474976710655)
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)
    return digest.to_bytes(48 // 8, 'little')


def crc_unknown(input: List[BitVec]) -> int:
    poly_degree = 48
    digest = BitVecVal((1 << poly_degree) - 1, 48)
    flip = BitVecVal(0xf9fdd219bc58, 48)
    for b in input:
        digest = digest ^ Int2BV(BV2Int(b), 48)
        for _ in range(8):
            digest = LShR(digest, 1) ^ If(digest & 1 == 1, flip, 0)
    return digest ^ (1 << poly_degree) - 1


def hash_unknown(input: List[BitVec]) -> bytes:
    digest = crc_unknown(input)
    u2, u1, u0 = 0xDfffffffffff, 0xFfffffffffff, 0xFfffffffffff
    assert (u2, u1, u0) == (246290604621823, 281474976710655, 281474976710655)
    digest = digest * (digest * u2 + u1) + u0
    return digest

def gen_content(length: int, hash_val:bytes, chars:List[int],  known:bytes) -> bytes:
    solver = Solver()
    content = [BitVec(f'content_{i}', 8) for i in range(length - len(known))] + [BitVecVal(b, 8) for b in known]
    solver.add(content[-len(known) - 2] >= 0x00)
    solver.add(content[-len(known) - 2] <= 0x20)
    solver.add(content[-len(known) - 2] != 0x0a)
    solver.add(content[-len(known) - 2] != 0x0d)

    for b in content[:-len(known)-2]:
        solver.add(And(b >= 0x00, b <= 0x7e, b != 0x0a, b != 0x0d))

    solver.add(hash_unknown(content) == int.from_bytes(hash_val, 'little'))

    contents = []

    for val in tqdm(chars):
        solver.push()
        solver.add(content[-len(known) - 1] == val)
        res = solver.check()
        if res != sat:
            print(f'Unsat: {res}')
            result = b''
        else:
            model = solver.model()
            if len(known):
                result = bytes([model[c].as_long() for c in content[0:-len(known)]]) + known
            else:
                result = bytes([model[c].as_long() for c in content])
        contents.append(result.decode())
        solver.pop()
    
    solver.reset()
    return contents

def req(content_list):
    filecontent = '\n'.join(content_list).encode()

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

expected_hash = b85decode('answer_c')
assert len(expected_hash) == 6
assert b85encode(expected_hash) == b'answer_c'

# filecontent = []
# for length in tqdm(range(97, 0, -1)):
#     filecontent.append(gen_content(length, expected_hash, ord('}'), b'').decode())
# hash_list = gethash(filecontent)

length = 64
chars = range(33, 118)
known = b'pfEmUY_EmAOdb3c6'
for pos in range(length - len(known) -  1, 0, -1):
    print(f'pos = {pos}, known = {known}')
    filecontent = gen_content(length, expected_hash, chars, known)
    hash_list = req(filecontent)
    for w, val in zip(hash_list, chars):
        if w is not None and w <= 0x20:
            known = bytes([val]) + known
            break

print(known)
