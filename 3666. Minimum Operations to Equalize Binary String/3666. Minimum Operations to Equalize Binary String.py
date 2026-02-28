class Solution:
    def minOperations(self, s: str, k: int) -> int:
        length = len(s)
        zero_count = s.count('0')

        if zero_count == 0:
            return 0

        if length == k:
            return 1 if zero_count == length else -1

        one_count = length - zero_count
        untouched = length - k

        def ceil_div(a, b):
            return (a + b - 1) // b

        answers = []
        
        if (k - zero_count) % 2 == 0:
            ops_needed = max(
                ceil_div(zero_count, k),
                ceil_div(one_count, untouched)
            )
            if ops_needed % 2 == 0:
                ops_needed += 1
            answers.append(ops_needed)

        if zero_count % 2 == 0:
            ops_needed = max(
                ceil_div(zero_count, k),
                ceil_div(zero_count, untouched)
            )
            if ops_needed % 2 == 1:
                ops_needed += 1
            answers.append(ops_needed)

        return min(answers) if answers else -1

sol = Solution()
s = "110"
k = 1
print(sol.minOperations(s, k))
