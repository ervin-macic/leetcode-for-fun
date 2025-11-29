class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add_to_tail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove existing node
            self._remove(self.cache[key])

        # Insert new node at MRU
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)

        # Evict LRU if needed
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


capacity = 2
moves = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
obj = LRUCache(capacity)
for move in moves:
    if len(move) == 2:
        # A put
        obj.put(move[0],move[1])
    else:
        print(obj.get(move[0]))
