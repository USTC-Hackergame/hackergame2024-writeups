import pwn
import time
import base64

# pwn.context.log_level = 'debug'

conn = pwn.connect('202.38.93.141', 10338)

conn.recvuntil(b'token: ')
conn.sendline(b'[redacted]')
conn.recvuntil(b'dockerv:')
conn.sendline(b'pwd')
# conn.sendline(b'rz')
# proc = pwn.process(['sz', './alpine.gz'])
# try:
#     i = 0
#     while True:
#         i += 1
#         print('iter', i)
#         data = proc.recv()
#         print('send', len(data))
#         conn.send(data)
#         data1 = conn.recv()
#         print('recv', len(data1))
#         proc.write(data1)
# except EOFError:
#     pass
def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))

start = time.time()
with open('alpine.gz', 'rb') as f:
    data = f.read()
    lines = chunkstring(base64.b64encode(data), 1024)
    conn.sendline(b'cat >/tmp/tmp.base64 <<EOFEOFEOF')
    i = 0
    for line in lines:
        i += 1
        print(f'{i}/{len(lines)} ({i/len(lines)*100:.2f}%)')
        conn.sendline(line)
        conn.recvuntil(b'>')
    conn.sendline(b'EOFEOFEOF')
    conn.sendline(b'cd /tmp')
    conn.sendline(b'cat /tmp/tmp.base64 | base64 -d >/tmp/alpine.gz')
    conn.sendline(b'gunzip /tmp/alpine.gz')
    conn.sendline(b'sudo docker load </tmp/alpine')
    print(f'time: {time.time() - start:.2f}s')
conn.interactive()
