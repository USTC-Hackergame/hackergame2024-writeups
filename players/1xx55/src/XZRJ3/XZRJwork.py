'''
filename = "answer_b.py"

with open(filename,'r') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][:-1] #去掉末尾换行符

print([len(data[i]) for i in range(len(data))] )
print([(i+1,len(data[i]))if len(data[i])!=80 else None for i in range(len(data))])
'''

def crc(input: bytes) -> int:                                                   
    poly, poly_degree = 'BBBBbBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBbB', 48 
    assert len(poly) == poly_degree + 1 and poly[0] == poly[poly_degree] == 'B' 
    flip = sum(['b', 'B'].index(poly[i + 1]) << i for i in range(poly_degree)) 
    print("flip: " , bin(flip)) 
    digest = (1 << poly_degree) - 1                                             
    for b in input:                                                             
        digest = digest ^ b                                                     
        for _ in range(8):                                                      
            digest = (digest >> 1) ^ (flip if digest & 1 == 1 else 0)           
    return digest ^ (1 << poly_degree) - 1                                      
                                                                                
                                                                                
def hash(input: bytes) -> bytes:                                                
    digest = crc(input)                                                        
    u2, u1, u0 = 0xdbeEaed4cF43, 0xFDFECeBdeeD9, 0xB7E85A4E5Dcd                 
    assert (u2, u1, u0) == (241818181881667, 279270832074457, 202208575380941)  
    digest = (digest * (digest * u2 + u1) + u0) % (1 << 48)                     
    return digest.to_bytes(48 // 8, 'little')    

# 试图Z3求hash逆......

q1 ="q                                                                               "

from z3 import *
dige = int.from_bytes((bytes.fromhex("270350f6b044")),'little')
aftercrc = Int('cr')
s = Solver()
u2, u1, u0 = 0xdbeEaed4cF43, 0xFDFECeBdeeD9, 0xB7E85A4E5Dcd 
s.add(aftercrc >= 0)
s.add(aftercrc < (1<<48))
s.add((aftercrc * (aftercrc * u2 + u1) + u0) % (1 << 48) == dige)

if s.check() == sat:
    m = s.model()
    print(m[aftercrc])  # 打印变量x的值
else:
    print("无解")

