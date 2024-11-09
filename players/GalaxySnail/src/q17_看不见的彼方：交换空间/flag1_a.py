""""exec python3 $0
exit
"""
# 做题的时候我先用 #!/usr/bin/python3 作为 shebang 发现不行，然后我就换成这种
# polyglot 方案了，但实际上换成 #!/bin/python3 就行了

import os
import sys
import socket

def exchange_files(fd1, fd2, filesize, bufsize=4096):
    print(f"{filesize=}")
    assert filesize % bufsize == 0
    buf1 = bytearray(bufsize)
    buf2 = bytearray(bufsize)

    offset = 0
    while offset < filesize:
        size = os.preadv(fd1, [buf1], offset)
        assert size == bufsize
        size = os.preadv(fd2, [buf2], offset)
        assert size == bufsize
        size = os.pwrite(fd2, buf1, offset)
        assert size == bufsize
        size = os.pwrite(fd1, buf2, offset)
        assert size == bufsize
        offset += bufsize

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    sock.bind(b"\0foobar")

    fd = os.open("/space/file", os.O_RDWR)
    _, fds, *_ = socket.recv_fds(sock, 1024, 1)
    other_fd = fds[0]

    fsize1 = os.fstat(fd).st_size
    fsize2 = os.fstat(other_fd).st_size
    assert fsize1 == fsize2

    exchange_files(fd, other_fd, fsize1)

main()
