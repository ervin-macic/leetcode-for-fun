class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        smallest = s
        visited = {s}
        queue = deque([s])

        while queue:
            current = queue.popleft()
            smallest = min(smallest, current)
            # Strings are immutable in Python so make list of chars from string for easier handling
            after_a = list(current)
            for i in range(1, len(s), 2):
                after_a[i] = str((int(after_a[i]) + a) % 10)
            
            after_a = ''.join(after_a)
            if after_a not in visited:
                visited.add(after_a)
                queue.append(after_a)
            
            after_b = current[-b:] + current[0:-b]

            if after_b not in visited:
                visited.add(after_b)
                queue.append(after_b)

        return smallest
