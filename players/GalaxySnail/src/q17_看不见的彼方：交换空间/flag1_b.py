""""exec python3 $0
exit
"""
import os
import time
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
time.sleep(0.5)
sock.connect(b"\0foobar")
socket.send_fds(sock, [b"hello"], [os.open("/space/file", os.O_RDWR)])
