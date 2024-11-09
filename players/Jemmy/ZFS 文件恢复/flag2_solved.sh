#!/bin/sh
flag_key="hg2024_1141919810.233696969_2109876543.1357924680_zfs"
echo "46c518b175651d440771836987a4e7404f84b20a43cc18993ffba7a37106f508  -" > /tmp/sha256sum.txt
printf "%s" "$flag_key" | sha256sum --check /tmp/sha256sum.txt || exit 1
printf "flag{snapshot_%s}\n" "$(printf "%s" "$flag_key" | sha1sum | head -c 32)"
