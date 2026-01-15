from typing import List
import bisect


class IntervalCoverageTree:
    def __init__(self, coords: List[int]):
        self.coords = coords
        self.size = len(coords) - 1
        self.active = [0] * (self.size * 4)
        self.length = [0] * (self.size * 4)

    def _recalc(self, node: int, left: int, right: int):
        if self.active[node] > 0:
            self.length[node] = self.coords[right + 1] - self.coords[left]
        elif left == right:
            self.length[node] = 0
        else:
            self.length[node] = (
                self.length[node * 2 + 1] + self.length[node * 2 + 2]
            )

    def modify(self, ql: int, qr: int, delta: int, left: int, right: int, node: int):
        if self.coords[right + 1] <= ql or self.coords[left] >= qr:
            return

        if ql <= self.coords[left] and self.coords[right + 1] <= qr:
            self.active[node] += delta
        else:
            mid = (left + right) // 2
            self.modify(ql, qr, delta, left, mid, node * 2 + 1)
            self.modify(ql, qr, delta, mid + 1, right, node * 2 + 2)

        self._recalc(node, left, right)

    def covered_length(self) -> int:
        return self.length[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sweep_events = []
        x_coords = set()

        for sx, sy, side in squares:
            sweep_events.append((sy, 1, sx, sx + side))
            sweep_events.append((sy + side, -1, sx, sx + side))
            x_coords.add(sx)
            x_coords.add(sx + side)

        xs = sorted(x_coords)
        tree = IntervalCoverageTree(xs)
        sweep_events.sort()

        cumulative_area = []
        horizontal_cover = []

        total = 0.0
        prev_y = sweep_events[0][0]

        for y, typ, lx, rx in sweep_events:
            covered = tree.covered_length()
            total += covered * (y - prev_y)

            tree.modify(lx, rx, typ, 0, tree.size - 1, 0)

            cumulative_area.append(total)
            horizontal_cover.append(tree.covered_length())
            prev_y = y

        half_area = (total + 1) // 2
        idx = bisect.bisect_left(cumulative_area, half_area) - 1

        base_area = cumulative_area[idx]
        width = horizontal_cover[idx]
        base_y = sweep_events[idx][0]

        return base_y + (total - 2 * base_area) / (2.0 * width)
