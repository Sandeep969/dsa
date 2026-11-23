# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                # one set, tagged keys for row / col / box
                keys = [("r", r, v), ("c", c, v), ("b", r // 3, c // 3, v)]
                for k in keys:
                    if k in seen:
                        return False
                    seen.add(k)
        return True


def parse(rows):
    return [list(row) for row in rows]


if __name__ == "__main__":
    s = Solution()
    valid = parse([
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ])
    assert s.isValidSudoku(valid)

    # same board but top-left 5 changed to 8, clashes in column 0 and box 0
    bad = [row[:] for row in valid]
    bad[0][0] = "8"
    assert not s.isValidSudoku(bad)

    empty = [["."] * 9 for _ in range(9)]
    assert s.isValidSudoku(empty)

    # row duplicate
    row_dup = [["."] * 9 for _ in range(9)]
    row_dup[4][0] = row_dup[4][8] = "7"
    assert not s.isValidSudoku(row_dup)

    # column duplicate
    col_dup = [["."] * 9 for _ in range(9)]
    col_dup[0][3] = col_dup[8][3] = "2"
    assert not s.isValidSudoku(col_dup)

    # box duplicate, different row and column
    box_dup = [["."] * 9 for _ in range(9)]
    box_dup[6][6] = box_dup[8][8] = "9"
    assert not s.isValidSudoku(box_dup)

    # same digit in different boxes/rows/cols is fine
    spread = [["."] * 9 for _ in range(9)]
    spread[0][0] = spread[4][4] = spread[8][8] = "1"
    assert s.isValidSudoku(spread)

    print("ok")
