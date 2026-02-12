from collections import defaultdict, deque
from typing import List


class LazyTag:
    def __init__(self):
        self.delta = 0

    def merge(self, other):
        self.delta += other.delta
        return self

    def active(self):
        return self.delta != 0

    def reset(self):
        self.delta = 0


class SegmentTreeNode:
    def __init__(self):
        self.lo = 0
        self.hi = 0
        self.tag = LazyTag()


class SegmentTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.nodes = [SegmentTreeNode() for _ in range(self.size * 4 + 5)]
        self._build(nums, 1, self.size, 1)

    def range_add(self, left, right, value):
        tag = LazyTag()
        tag.delta = value
        self._update(left, right, tag, 1, self.size, 1)

    def query_last(self, start, value):
        if start > self.size:
            return -1
        return self._query(start, self.size, value, 1, self.size, 1)

    def _apply(self, idx, tag):
        self.nodes[idx].lo += tag.delta
        self.nodes[idx].hi += tag.delta
        self.nodes[idx].tag.merge(tag)

    def _push(self, idx):
        if self.nodes[idx].tag.active():
            tag = LazyTag()
            tag.delta = self.nodes[idx].tag.delta
            self._apply(idx * 2, tag)
            self._apply(idx * 2 + 1, tag)
            self.nodes[idx].tag.reset()

    def _pull(self, idx):
        self.nodes[idx].lo = min(
            self.nodes[idx * 2].lo, self.nodes[idx * 2 + 1].lo
        )
        self.nodes[idx].hi = max(
            self.nodes[idx * 2].hi, self.nodes[idx * 2 + 1].hi
        )

    def _build(self, nums, left, right, idx):
        if left == right:
            val = nums[left - 1]
            self.nodes[idx].lo = val
            self.nodes[idx].hi = val
            return
        mid = left + ((right - left) >> 1)
        self._build(nums, left, mid, idx * 2)
        self._build(nums, mid + 1, right, idx * 2 + 1)
        self._pull(idx)

    def _update(self, ql, qr, tag, left, right, idx):
        if ql <= left and right <= qr:
            self._apply(idx, tag)
            return
        self._push(idx)
        mid = left + ((right - left) >> 1)
        if ql <= mid:
            self._update(ql, qr, tag, left, mid, idx * 2)
        if qr > mid:
            self._update(ql, qr, tag, mid + 1, right, idx * 2 + 1)
        self._pull(idx)

    def _query(self, ql, qr, value, left, right, idx):
        if self.nodes[idx].lo > value or self.nodes[idx].hi < value:
            return -1
        if left == right:
            return left
        self._push(idx)
        mid = left + ((right - left) >> 1)
        if qr >= mid + 1:
            res = self._query(ql, qr, value, mid + 1, right, idx * 2 + 1)
            if res != -1:
                return res
        if left <= qr and mid >= ql:
            return self._query(ql, qr, value, left, mid, idx * 2)
        return -1


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        occurrences = defaultdict(deque)

        def sign(x):
            return 1 if x % 2 == 0 else -1

        n = len(nums)
        best = 0
        prefix = [0] * n
        prefix[0] = sign(nums[0])
        occurrences[nums[0]].append(1)

        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if not occurrences[nums[i]]:
                prefix[i] += sign(nums[i])
            occurrences[nums[i]].append(i + 1)

        tree = SegmentTree(prefix)

        for i in range(n):
            pos = tree.query_last(i + best, 0)
            best = max(best, pos - i)
            occurrences[nums[i]].popleft()
            nxt = n + 1
            if occurrences[nums[i]]:
                nxt = occurrences[nums[i]][0]
            tree.range_add(i + 1, nxt - 1, -sign(nums[i]))

        return best
