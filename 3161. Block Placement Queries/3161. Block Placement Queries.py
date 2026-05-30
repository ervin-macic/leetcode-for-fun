from sortedcontainers import SortedList

MAX_INT = 50_000

class SegmentTree:
    def __init__(self, arr, f, identity):
        self.n = len(arr)
        self.f = f
        self.identity = identity
        self.tree = [identity] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, left, right):
        if left == right:
            self.tree[node] = arr[left]
            return

        mid = (left + right) // 2
        self._build(arr, 2 * node, left, mid)
        self._build(arr, 2 * node + 1, mid + 1, right)

        self.tree[node] = self.f(
            self.tree[2 * node],
            self.tree[2 * node + 1]
        )

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, left, right, ql, qr):
        if qr < left or ql > right:
            return self.identity

        if ql <= left and right <= qr:
            return self.tree[node]

        mid = (left + right) // 2
        return self.f(
            self._query(2 * node, left, mid, ql, qr),
            self._query(2 * node + 1, mid + 1, right, ql, qr)
        )

    def update(self, idx, value):
        self._update(1, 0, self.n - 1, idx, value)

    def _update(self, node, left, right, idx, value):
        if left == right:
            self.tree[node] = value
            return

        mid = (left + right) // 2

        if idx <= mid:
            self._update(2 * node, left, mid, idx, value)
        else:
            self._update(2 * node + 1, mid + 1, right, idx, value)

        self.tree[node] = self.f(
            self.tree[2 * node],
            self.tree[2 * node + 1]
        )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        sl = SortedList([0, MAX_INT])
        arr = [0] * (MAX_INT + 1)
        arr[MAX_INT] = MAX_INT
        seg = SegmentTree(arr, max, 0)
        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_right(x)
                if idx == len(sl):
                    idx -= 1
                r = sl[idx]
                l = sl[idx - 1]
                seg.update(x, x - l)
                seg.update(r, r - x)
                sl.add(x)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x)
                if idx == len(sl):
                    idx -= 1
                pre = sl[idx - 1]
                max_space = max(
                    x - pre,
                    seg.query(0, pre)
                )
                ans.append(max_space >= sz)
        return ans