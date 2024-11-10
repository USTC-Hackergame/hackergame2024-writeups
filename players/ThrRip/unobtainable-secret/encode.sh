#!/bin/bash

# Make sure _vw is a multiple of 8
_vw=
# Make sure _vh is at least 1 less than terminal lines
_vh=

mkdir secret
cd secret
cp /secret .
# Split the secret into chunks
split -a 3 -b $(($_vw * $_vh / 8)) -d secret secret.
# Convert the chunks to binary represented with black and white blocks
# "█" can be obtained from echo -e '\u2588'
for c in secret.*; do basenc --base2msbf -w $_vw $c | sed -E 's/0/ /g; s/1/█/g' > $c.txt; done
