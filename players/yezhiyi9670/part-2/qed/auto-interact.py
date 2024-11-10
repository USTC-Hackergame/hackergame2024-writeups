import pexpect
from pexpect import popen_spawn
import re

token = '114514:[redacted]'

process = pexpect.popen_spawn.PopenSpawn('nc 202.38.93.141 14514')
process.expect('Please input your token:')
process.sendline(token)

payload_head_1 = '2*3**(1/2)*(3*(1/(3+x*x))-(1-x*x/3)*(1+(x*x/3)**2)*(1+(x*x/3)**4)*(1+(x*x/3)**8)*(1+(x*x/3)**16)*(1+(x*x/3)**32)+1336924087160732342156363814611099537023584771936953706677720480762397655142327936/1287978018036015777334466551354189481340554850313375/3**63*129*x**128)-129*x**128*'
payload_head_2 = '2*3**(1/2)*(3*(1/(3+x*x))-(1-x*x/3)*(1+(x*x/3)**2)*(1+(x*x/3)**4)*(1+(x*x/3)**8)*(1+(x*x/3)**16)*(1+(x*x/3)**32)+1336924087160732342156363814611099537023584771936953706677720480762397655142327936/1287978018036015777334466551354189481340554850313375/3**63*129*x**128)-65*x**64*'
payload_head = payload_head_1

for difficulty in range(40):
    process.expect_exact('Enter the function f(x)')
    before: str = process.before.decode()
    print('===', difficulty)
    print(before)
    head_p = before.index('>=')
    before = before[head_p+2:]
    tail_p = before.index('\n')
    fract = before[0:tail_p]
    print(fract)
    process.sendline(payload_head + fract)
    if difficulty == 21:
        payload_head = payload_head_2 # Switch to the slower payload

process.expect(pexpect.EOF)
print(process.before)
