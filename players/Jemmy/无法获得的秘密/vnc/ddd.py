with open('secret', 'rb') as f:
    data = f.read()[:512*1024]
with open('secret_sliced', 'wb') as f:
    f.write(data)