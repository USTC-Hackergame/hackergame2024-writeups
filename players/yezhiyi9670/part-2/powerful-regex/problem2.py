MODULO = 13
BITS_MAX = 64
bit_significance = [1 % MODULO] * BITS_MAX
for i in range(1, BITS_MAX):
    bit_significance[i] = (bit_significance[i-1] * 2) % MODULO

def common_prefix_suffix_len(items: list[str]):
    prefix_len = 0
    suffix_len = 0
    k = 0
    for i in range(0, min(map(len, items))):
        if items[0][i] == '(': k += 1
        if items[0][i] == ')': k -= 1
        if len(set(map(lambda s: s[i], items))) <= 1:
            if k == 0: prefix_len = i + 1
        else:
            break
    k = 0
    for i in range(1, min(map(len, items)) + 1):
        if items[0][-i] == '(': k += 1
        if items[0][-i] == ')': k -= 1
        if len(set(map(lambda s: s[-i], items))) <= 1:
            if k == 0: suffix_len = i
        else:
            break
    return prefix_len, suffix_len

def pack_choices(items: list[str]):
    if len(items) == 0:
        return ''
    
    prefix_len, suffix_len = common_prefix_suffix_len(items)
    min_len = min(map(len, items))
    suffix_len = min(min_len - prefix_len, suffix_len)
    prefix = items[0][0:prefix_len]
    suffix = items[0][-suffix_len if suffix_len != 0 else len(items[0]):]
    items = set([
        item[prefix_len:-suffix_len if suffix_len != 0 else len(item)]
        for item in items
    ])
    
    if len(items) == 1:
        return prefix + next(iter(items)) + suffix
    return prefix + (
        ('(' + '|'.join(sorted(items)) + ')')
    ) + suffix

def concat_packed_choices(a, b):
    if a == '' or b == '':
        return ''
    return a + b

rest_z_cache = {}
# Should return '' on failure
def rest_z(z: bool, msb: int, lsb: int, rem: int):
    global rest_z_cache
    
    cache_sig = (z, msb-lsb+1, bit_significance[lsb], rem)
    cache = rest_z_cache.get(cache_sig)
    if cache != None:
        return cache
    
    assert msb >= lsb
    assert 0 <= rem < MODULO
    choices = []
    if msb == lsb:
        if rem == 0:
            if z: choices.append('')
            else: choices.append('0')  # The starting of a complete number just cannot be zero
        if rem == bit_significance[lsb]:
            choices.append('1')
        rest_z_cache[cache_sig] = cache = pack_choices(choices)
        return cache
    mid_low = (lsb + msb) // 2
    mid_high = mid_low + 1
    for c in range(MODULO):
        res = concat_packed_choices(
            rest_z(z, msb, mid_high, (-c) % MODULO),  # Negative modulo is safe in python
            rest_z(False, mid_low, lsb, (c + rem) % MODULO)
        )
        if res != '':
            choices.append(res)
    if z:
        res = rest_z(z, mid_low, lsb, rem % MODULO)
        if res != '':
            choices.append(res)
    rest_z_cache[cache_sig] = cache = pack_choices(choices)
    return cache

# print(pack_choices(['01', '01', '01']))
# print(pack_choices(['01', '01', '011', '01121']))
# print(pack_choices(['01(330)', '01(320)', '01(340)']))
print('2')
print(rest_z(True, 63, 0, 0))
