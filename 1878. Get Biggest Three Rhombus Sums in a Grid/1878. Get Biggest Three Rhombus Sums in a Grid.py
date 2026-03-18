from typing import List


class TopThree:
    def __init__(self):
        self.values = [0, 0, 0]

    def add(self, val: int):
        a, b, c = self.values

        if val in (a, b, c):
            return

        if val > a:
            self.values = [val, a, b]
        elif val > b:
            self.values = [a, val, b]
        elif val > c:
            self.values[2] = val

    def result(self) -> List[int]:
        return [v for v in self.values if v != 0]


class Solution:
    def _build_diagonal_prefix(self, grid):
        rows, cols = len(grid), len(grid[0])

        diag_left = [[0] * (cols + 2) for _ in range(rows + 1)]
        diag_right = [[0] * (cols + 2) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                val = grid[r - 1][c - 1]
                diag_left[r][c] = diag_left[r - 1][c - 1] + val
                diag_right[r][c] = diag_right[r - 1][c + 1] + val

        return diag_left, diag_right

    def _rhombus_sum(self, grid, dl, dr, top_r, top_c, bottom_r):
        mid_r = (top_r + bottom_r) // 2
        half = (bottom_r - top_r) // 2

        left_c = top_c - half
        right_c = top_c + half

        top = (top_r, top_c)
        bottom = (bottom_r, top_c)
        left = (mid_r, left_c)
        right = (mid_r, right_c)

        total = (
            (dr[left[0] + 1][left[1] + 1] - dr[top[0]][top[1] + 2]) +
            (dl[right[0] + 1][right[1] + 1] - dl[top[0]][top[1]]) +
            (dl[bottom[0] + 1][bottom[1] + 1] - dl[left[0]][left[1]]) +
            (dr[bottom[0] + 1][bottom[1] + 1] - dr[right[0]][right[1] + 2])
        )

        corners = (
            grid[top[0]][top[1]] +
            grid[bottom[0]][bottom[1]] +
            grid[left[0]][left[1]] +
            grid[right[0]][right[1]]
        )

        return total - corners

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        diag_left, diag_right = self._build_diagonal_prefix(grid)

        best = TopThree()

        for r in range(rows):
            for c in range(cols):

                best.add(grid[r][c])  # single cell rhombus

                size = r + 2
                while size < rows:
                    if (size - r) % 2 != 0:
                        size += 1
                        continue

                    half = (size - r) // 2
                    if c - half < 0 or c + half >= cols:
                        break

                    val = self._rhombus_sum(grid, diag_left, diag_right, r, c, size)
                    best.add(val)

                    size += 2

        return best.result()