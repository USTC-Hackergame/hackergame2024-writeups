""""exec python3 $0
exit
"""
import os
import socket
import ctypes

libc = ctypes.CDLL(None, use_errno=True)
libc.syscall.restype = ctypes.c_long
libc.syscall.argtypes = [
    ctypes.c_long,  # syscall number
    ctypes.c_int,  # fd
    ctypes.c_int,  # mode
    ctypes.c_uint64,  # offset
    ctypes.c_uint64,  # len
]
SYS_fallocate = 285
FALLOC_FL_KEEP_SIZE  = 0x01
FALLOC_FL_PUNCH_HOLE = 0x02

def fallocate(fd, mode, offset, length):
    res = libc.syscall(SYS_fallocate, fd, mode, offset, length)
    if res < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return res

def move_file(src_fd, dst_fd, bufsize=4096):
    filesize = os.fstat(src_fd).st_size
    print(f"{src_fd=}, {filesize=}")
    assert filesize % bufsize == 0
    buf = bytearray(bufsize)

    offset = 0
    while offset < filesize:
        size = os.preadv(src_fd, [buf], offset)
        assert size == bufsize
        size = os.pwrite(dst_fd, buf, offset)
        assert size == bufsize
        fallocate(
            src_fd,
            FALLOC_FL_KEEP_SIZE | FALLOC_FL_PUNCH_HOLE,
            offset,
            bufsize,
        )
        offset += bufsize

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    sock.bind(b"\0foobar")
    _, fds, *_ = socket.recv_fds(sock, 1024, 3)
    dst0, src1, src2 = fds

    src0 = os.open("/space/file", os.O_RDWR)
    dst1 = os.open("/space/file1", os.O_RDWR | os.O_CREAT)
    dst2 = os.open("/space/file2", os.O_RDWR | os.O_CREAT)

    move_file(src0, dst0)
    move_file(src1, dst1)
    move_file(src2, dst2)

    with open("/space/file1", "ab"), open("/space/file2", "ab"):
        pass

main()
