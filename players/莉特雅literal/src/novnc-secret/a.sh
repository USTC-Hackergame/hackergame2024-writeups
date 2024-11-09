set -x
gcc -flto -Os -Wl,--gc-sections encoder.c -o encoder
strip --strip-all --remove-section=.comment --remove-section=.note encoder
python3 fee.py encoder | python3
xrandr --output VNC-0 --mode 1920x1080
firefox result.png
