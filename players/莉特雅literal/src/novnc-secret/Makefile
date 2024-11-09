.PHONY: all
all: payload.b64

CFLAGS = -fsanitize=address

ARCHIVER = cpio
FILES = encoder.c stb_image_write.h fee.py a.sh

encoder: encoder.c
	$(CC) $(CFLAGS) -I. $^ -o $@

payload.b64: payload.$(ARCHIVER).zst
	base64 $< > $@
	echo "result `wc -l $@ | cut -d ' ' -f 1` lines"

# -f for override
payload.$(ARCHIVER).zst: payload.$(ARCHIVER)
	zstd --ultra -20 -f $< -o $@

payload.tar: $(FILES)
	tar cf $@ $^

#################################################
# cpio

payload.cpio: $(FILES)
	find $^ | cpio -o > $@

.PHONY: clean
clean:
	rm -f payload.tar* payload.cpio* payload.b64 *.zst encoder
