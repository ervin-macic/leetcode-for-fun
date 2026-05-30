from math import gcd
class SegmentTree:
    # f function applied (like max, sum, gcd...) 
    # f(identity, a) = a must hold so identity for max would be float('-inf') because
    # f must be associative for segment tree to work, i.e. f(f(a,b), c) = f(a, f(b,c))
    # interesting remark: A segment tree works whenever (S, f, e) form a monoid (f assoc. e iden.) 
    def __init__(self, arr, f, identity):
        self.n = len(arr)
        self.f = f
        self.identity = identity 
        self.tree = [identity] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)
    
    # build a segment tree rooted at node for arr[left, right] (this subtree is a segment tree for arr[left, right])
    def _build(self, arr, node, left, right):
        # leaf
        if left == right:
            self.tree[node] = arr[left]
            return
        
        # non-leaf
        mid = (left + right) // 2
        # [left mid] [mid + 1 right]
        self._build(arr, 2 * node, left, mid)
        self._build(arr, 2 * node + 1, mid + 1, right)
        
        # val(parent) = f(val(left child), val(right child))
        self.tree[node] = self.f(
            self.tree[2 * node],
            self.tree[2 * node + 1]
        )

    # What is f([2, 5])? i.e. f(2,3,4,5) so inclusive [ql, qr]
    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)
    
    def _query(self, node, left, right, ql, qr):
        # No overlap [ql qr] [left right] or [left right] [ql qr]
        if qr < left or right < ql:
            return self.identity
        
        # Complete overlap [ql [left right] qr]
        if ql <= left and right <= qr:
            return self.tree[node]
        
        # Partial overlap [ql [left qr] right] or [left [ql right] qr]
        mid = (left + right) // 2
        return self.f(
            self._query(2 * node, left, mid, ql, qr),
            self._query(2 * node + 1, mid + 1, right, ql, qr)
        )
    
    # set arr[idx] = value
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
            self._update(2 * node + 1, mid + 1, right, idx ,value)
        
        self.tree[node] = self.f(
            self.tree[2 * node],
            self.tree[2 * node + 1]
        )

arr = [5,8,6,3,2,7,2,6]
maxSegmentTree = SegmentTree(
    arr,
    f = max,
    identity = float('-inf')
)

sumSegmentTree = SegmentTree(
    arr,
    f = lambda a, b: a + b,
    identity = 0
)

gcdSegmentTree = SegmentTree(
    arr,
    f = gcd,
    identity = 0
)

# max in [6,3,2,7] is 7
print(maxSegmentTree.query(2, 5))
maxSegmentTree.update(5, 1)
# max in [6,3,2,1] is 6
print(maxSegmentTree.query(2, 5))