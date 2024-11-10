#!/bin/bash

# The second to start
_s=$1
# Interval (seconds) between chunks
_i=$2

[ $_s -gt $((10#$(date +%S))) ] && sleep $(($_s - $((10#$(date +%S))) - 1)).$((1000 - 10#$(date +%N | head -c 3)))

for c in secret.*.txt; do clear; cat $c; echo -n $c; sleep $_i; done
echo
