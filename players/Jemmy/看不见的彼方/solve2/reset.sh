#!/bin/bash

gcc Alice.c -o Alice
gcc Bob.c -o Bob
rm ./A/file*
rm ./B/file*
dd if=/dev/urandom bs=1M count=128 > ./A/file
cp ./A/file ./A/file.bak
dd if=/dev/urandom bs=1M count=64 > ./B/file1
cp ./B/file1 ./B/file1.bak
dd if=/dev/urandom bs=1M count=64 > ./B/file2
cp ./B/file2 ./B/file2.bak

