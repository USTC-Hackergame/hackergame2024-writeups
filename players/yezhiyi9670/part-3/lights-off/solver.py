import numpy
from bitsets import bitset

n = 5

def take_in_puzzle(n: int, bin_str: str):
    assert len(bin_str) == n ** 3, 'Mismatching puzzle size'
    lights_array = numpy.array(list(map(lambda x: int(x), [*bin_str])), dtype=numpy.uint8).reshape((n, n, n))
    return lights_array

def bit_at(s: int, i: int):
    return 1 if (s & (1 << i)) else 0

def bits_between(s: int, i: int, j: int):
    return (s >> i) & ((1 << (j - i)) - 1)

def replace_bits_between(s: int, i: int, j: int, t: int):
    left = ((s >> j) << (j - i)) | (t & ((1 << (j - i)) - 1))
    return (left << i) | (s & ((1 << i) - 1))

coeff_len = n ** 2 + 1  # the 2^0 bit is the constant term

'Shift the coeff bitset left/right/forward/backward'
def shift_floor_coeff(coeff: int, t: int):
    assert 0 <= t <= 4
    if t == 0:
        return coeff
    const = bit_at(coeff, 0)
    coeff >>= 1
    if 1 <= t <= 2:
        # shift left/right
        for index in range(n):
            i = index * n
            j = i + n
            row = bits_between(coeff, i, j)
            if t == 1:
                row >>= 1
            else:
                row <<= 1
            coeff = replace_bits_between(coeff, i, j, row)
        return (coeff << 1) | const
    else:
        # shift forward/backward
        if t == 3:
            coeff >>= n
        else:
            coeff <<= n
        return bits_between((coeff << 1) | const, 0, coeff_len)

'Get the coeff bitset of the first-floor location'
def coeff_on_loc(x: int, y: int):
    return 1 << (y * n + x + 1)

'Format coeff'
def fmt_coeff(coeff: int):
    return bin(coeff)[2:].zfill(coeff_len)

# test_set = 0b00001000100010001000100001
# for i in range(5):
#     print(bin(shift_floor_coeff(test_set, i))[2:].zfill(coeff_len))

n = int(input("n: "))
coeff_len = n ** 2 + 1
puzzle = input('puzzle: ')
puzzle = take_in_puzzle(n, puzzle)

state_matrix = puzzle.tolist()
op_matrix = numpy.zeros_like(puzzle).tolist()

# Click on a position
def apply_coeff_to(x, y, l, op):
    global state_matrix, op_matrix
    op_matrix[l][x][y] ^= op
    state_matrix[l][x][y] ^= op
    if l - 1 >= 0:
        state_matrix[l-1][x][y] ^= op
    if l + 1 < n:
        state_matrix[l+1][x][y] ^= op
    if x - 1 >= 0:
        state_matrix[l][x-1][y] ^= op
    if x + 1 < n:
        state_matrix[l][x+1][y] ^= op
    if y - 1 >= 0:
        state_matrix[l][x][y-1] ^= op
    if y + 1 < n:
        state_matrix[l][x][y+1] ^= op

# Apply the first-floor combinations to the first floor
if n > 0:
    for x in range(n):
        for y in range(n):
            op = coeff_on_loc(x, y)
            apply_coeff_to(x, y, 0, op)
            
# Start inference from the second floor
for l in range(1, n):
    for x in range(n):
        for y in range(n):
            op = state_matrix[l-1][x][y]         # This is the last chance to clear the previous floor
            apply_coeff_to(x, y, l, op)          # Apply the action
            assert state_matrix[l-1][x][y] == 0  # Ensures the previous floor is cleared

# The final floor must be cleared. Collect the equations first.
equations = []
for x in range(n):
    for y in range(n):
        equations.append(state_matrix[n-1][x][y])

print('Equations pre-elimination:')
for eq in equations:
    print(fmt_coeff(eq))

# Gaussian elimination, start from the leftmost bit and stop at the second rightmost.
c = coeff_len - 1
i = 0
while c >= 0 and i < len(equations):
    j = i
    # Find a row with non-zero bit at c
    for j in range(i, len(equations)):
        if bit_at(equations[j], c):
            break
    else:
        c -= 1
        continue  # No elimination is needed on this bit
    equations[i], equations[j] = equations[j], equations[i]  # Yank the eliminator
    # Now eliminate the rest
    for j in range(i + 1, len(equations)):
        if bit_at(equations[j], c):
            equations[j] ^= equations[i]
    c -= 1
    i += 1

print('Equations:')
for eq in equations:
    print(fmt_coeff(eq))

flag_no_solution = False
solution_set = 0b1  # The constant is already solved to 1
for i in range(len(equations) - 1, -1, -1):
    c = 0
    for c in range(coeff_len - 1, 0, -1):
        if bit_at(equations[i], c):
            break
    # Now solve the bit at c
    bit_coeff = bit_at(equations[i], c)
    assert bit_at(solution_set, c) == 0, 'The bit to solve is already set'
    required_value = (equations[i] & solution_set).bit_count() & 1  # The bit at c is always 0
    if required_value and not bit_coeff:
        flag_no_solution = True
        break
    # If bit_coeff is 1, this is right. If not, the solution can be anything we like. Also must be right for all-zero rows.
    solution_value = required_value
    solution_set |= (solution_value << c)
    
if flag_no_solution:
    print('No solution!')
    exit()

print('Solution:')
print(fmt_coeff(solution_set))

for x in range(n):
    for y in range(n):
        assert ((state_matrix[n-1][x][y] & solution_set).bit_count() & 1) == 0

action_str = ''
for l in range(n):
    for x in range(n):
        for y in range(n):
            action_str += str(1 & (op_matrix[l][x][y] & solution_set).bit_count())

print('Actions:')
print(action_str)
