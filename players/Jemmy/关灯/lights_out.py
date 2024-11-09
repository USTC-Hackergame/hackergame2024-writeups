import numpy
import zlib
import base64
import time
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def convert_switch_array_to_lights_array(switch_array: numpy.array) -> numpy.array:
    lights_array = numpy.zeros_like(switch_array)
    lights_array ^= switch_array
    lights_array[:-1, :, :] ^= switch_array[1:, :, :]
    lights_array[1:, :, :] ^= switch_array[:-1, :, :]
    lights_array[:, :-1, :] ^= switch_array[:, 1:, :]
    lights_array[:, 1:, :] ^= switch_array[:, :-1, :]
    lights_array[:, :, :-1] ^= switch_array[:, :, 1:]
    lights_array[:, :, 1:] ^= switch_array[:, :, :-1]
    return lights_array

def generate_puzzle(n: int) -> numpy.array:
    random_bytes = get_random_bytes((n**3) // 8 + 1)
    switch_array = numpy.unpackbits(numpy.frombuffer(random_bytes, dtype=numpy.uint8))[:(n**3)].reshape(n, n, n)
    lights_array = convert_switch_array_to_lights_array(switch_array)
    return lights_array

def compress_and_encrypt(data: str, key: bytes) -> str:
    compressed_data = zlib.compress(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = base64.b64encode(cipher.iv + cipher.encrypt(pad(compressed_data, AES.block_size))).decode('utf-8')
    return encrypted_data

def decrypt_and_decompress(data: str, key: bytes) -> str:
    data = base64.b64decode(data.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv=data[:AES.block_size])
    decrypted_data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
    decompressed_data = zlib.decompress(decrypted_data).decode('utf-8')
    return decompressed_data

difficulty = int(input("Enter difficulty level (1~4): "))

if difficulty == 1:
    n = 3
    time_limit = 200
elif difficulty == 2:
    n = 5
    time_limit = 200
elif difficulty == 3:
    n = 11
    time_limit = 200
elif difficulty == 4:
    n = 149
    time_limit = 10
else:
    raise ValueError("Invalid difficulty level")

lights_array = generate_puzzle(n)
lights_string = "".join(map(str, lights_array.flatten().tolist()))
key = get_random_bytes(16)
encrypted_data = compress_and_encrypt(lights_string, key)
assert lights_string == decrypt_and_decompress(encrypted_data, key)

# print the puzzle
if difficulty != 4:
    start_time = time.time()
    print(lights_string)
else:
    print(encrypted_data)
    input("Press [Enter] to reveal the decryption key and start the timer: ")
    start_time = time.time()
    print(key.hex())  # Hint: you can use bytes.fromhex method to convert the hex string to bytes

# get the answer
if difficulty != 4:
    answer = input("Enter your answer: ").strip()
    stop_time = time.time()
    if stop_time - start_time > time_limit:
        raise RuntimeError("Time limit exceeded")
else:
    commitment = input("Enter SHA-256 hash of your answer as soon as possible: ")
    stop_time = time.time()
    if stop_time - start_time > time_limit:
        raise RuntimeError("Time limit exceeded")
    answer = input("Enter your answer: ").strip()
    sha256_of_answer = hashlib.sha256(answer.encode('utf-8')).hexdigest()
    if sha256_of_answer != commitment:
        raise ValueError("Invalid commitment {} != {}".format(sha256_of_answer, commitment))

# check the answer
if len(answer) != n**3:
    raise ValueError("Invalid answer length {} != {}".format(len(answer), n**3))
if not all(map(lambda x: x in "01", answer)):
    raise ValueError("Invalid answer format (only 0 and 1 are allowed)")
switch_array = numpy.array(list(map(int, answer)), dtype=numpy.uint8).reshape(n, n, n)
actual_lights_array = convert_switch_array_to_lights_array(switch_array)
if not numpy.array_equal(lights_array, actual_lights_array, equal_nan=False):
    raise ValueError("Incorrect answer")

# print the flag
print(open(f"flag{difficulty}").read())
