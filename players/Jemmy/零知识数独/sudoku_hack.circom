pragma circom 2.0.0;

include "./node_modules/circomlib/circuits/comparators.circom";

template IsValidInput(){
  signal input value;
  signal output out;
  component upperBound = LessEqThan(4);
  upperBound.in[0] <== value;
  upperBound.in[1] <== 9;
  out <== upperBound.out;
}

template SudokuChecker(SIZE) {
  signal input in[SIZE];

  component is_equal[SIZE][SIZE];
  for (var i = 0;i < SIZE;i++) {
    for (var j = 0;j < SIZE;j++) {
      is_equal[i][j] = IsEqual();
    }
  }

  for (var i = 0; i < SIZE; i++) {
    for (var j = 0; j < SIZE; j++) {
      is_equal[i][j].in[0] <== in[i];
      is_equal[i][j].in[1] <== (i == j) ? 0 : in[j];
      is_equal[i][j].out === 0;
    }
  }
}

template Main(SIZE, SUBSIZE) {
  signal input unsolved_grid[SIZE][SIZE];
  signal input solved_grid[SIZE][SIZE];
  signal gt_zero_signals[SIZE][SIZE];

  component range_checkers[SIZE][SIZE][2];
  component row_checkers[SIZE];
  component col_checkers[SIZE];
  component submat_checkers[SIZE];

  for (var i = 0;i < SIZE;i++) {
    row_checkers[i] = SudokuChecker(SIZE);
    col_checkers[i] = SudokuChecker(SIZE);
    submat_checkers[i] = SudokuChecker(SIZE);
    for (var j = 0;j < SIZE;j++) {
      for (var k = 0;k < 2;k++) {
        range_checkers[i][j][k] = IsValidInput();
      }
    }
  }

  // check range and puzzle matching
  for (var i = 0;i < SIZE;i++) {
    for (var j = 0;j < SIZE;j++) {
      range_checkers[i][j][0].value <== solved_grid[i][j];
      range_checkers[i][j][0].out === 1;
      gt_zero_signals[i][j] <-- 1;
      gt_zero_signals[i][j] === 1;
      range_checkers[i][j][1].value <== unsolved_grid[i][j];
      range_checkers[i][j][1].out === 1;
      (unsolved_grid[i][j] - solved_grid[i][j]) * unsolved_grid[i][j] === 0;
    }
  }


  // Check rows
  for (var i = 0;i < SIZE;i++) {
    for (var j = 0;j < SIZE;j++) {
      row_checkers[i].in[j] <== solved_grid[i][j];
    }
  }

  // Check columns
  for (var i = 0;i < SIZE;i++) {
    for (var j = 0;j < SIZE;j++) {
      col_checkers[i].in[j] <== solved_grid[j][i];
    }
  }

  // Check submatrices
  for (var i = 0;i < SIZE;i += SUBSIZE) {
    for (var j = 0;j < SIZE;j += SUBSIZE) {
      for (var k = 0;k < SUBSIZE;k++) {
        for (var l = 0;l < SUBSIZE;l++) {
          submat_checkers[i + j / SUBSIZE].in[k*SUBSIZE + l] <== solved_grid[i + k][j + l];
        }
      }
    }
  }
}

component main  {public [unsolved_grid]} = Main(9, 3);