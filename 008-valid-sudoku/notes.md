# 8. Valid Sudoku (Medium)

https://leetcode.com/problems/valid-sudoku/

Check if a partly filled 9x9 board breaks any sudoku rule so far (no need to solve it).

- brute force: check each row, each column, each 3x3 box separately, 27 passes over 9 cells
- single pass: for every filled cell record (row, digit), (col, digit), (box, digit) in a set,
  if any is already there it's invalid
- box index is `(r // 3, c // 3)`, easy to get wrong if you try to flatten it to one number
- tag the keys ("r", "c", "b") so a row key never collides with a column key
- skip "." cells, only filled digits matter
- valid here doesn't mean solvable, just no duplicates

O(81) = O(1) time and space since the board is fixed size.
