#!/usr/bin/python3
import os
import sys
import socket
import time

pid = os.fork()
if pid > 0:
    # parent
    sys.exit()

# child
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8000))
time.sleep(114514)
