import json
from os import system

N = 9
# Checks whether it will be
# legal to assign num to the
# given row, col


def isSafe(grid, row, col, num):

    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */


def solveSudoku(grid, row, col):

    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True

    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0

    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:

        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(grid, row, col, num):

            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num

            # Checking for next possibility with next
            # column
            if solveSudoku(grid, row, col + 1):
                return True

        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False

# Driver Code


puzzle = [9, 0, 0, 0, 0, 0, 1, 0, 0, 
          8, 0, 0, 0, 0, 0, 2, 0, 0,
          7, 0, 0, 0, 0, 0, 3, 0, 0,
          0, 0, 1, 0, 0, 0, 0, 0, 6,
          0, 2, 0, 0, 0, 0, 0, 7, 0,
          0, 0, 3, 0, 0, 0, 0, 0, 0,
          0, 1, 0, 0, 0, 0, 0, 6, 0,
          0, 0, 2, 0, 0, 0, 0, 0, 7,
          0, 3, 0, 0, 0, 0, 0, 0, 0]

unsolved_grid = [puzzle[i:i+9] for i in range(0, 81, 9)]

# puzzle = [puzzle[i] if puzzle[i] != 0 else -1 for i in range(81)]
solved_grid = [puzzle[i:i+9] for i in range(0, 81, 9)]
solveSudoku(solved_grid, 0, 0)

print(unsolved_grid)
print(solved_grid)
data = {'unsolved_grid': unsolved_grid, 'solved_grid': solved_grid}
with open('input.json', 'w') as f:
    json.dump(data, f)

print('input.json created')

system('snarkjs calculatewitness sudoku_hack.wasm input.json')

system('snarkjs proof sudoku.zkey witness.wtns proof.json public.json')

system('snarkjs groth16 verify verification_key.json public.json proof.json')
