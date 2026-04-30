class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        size = len(grid)
        if size <= 1:
            return 0

        prefix = [[0] * (size + 1) for _ in range(size)]
        for col in range(size):
            running = 0
            for row in range(size):
                running += grid[row][col]
                prefix[col][row + 1] = running

        last_dp = [[0] * (size + 1) for _ in range(size + 1)]
        best_left = [[0] * (size + 1) for _ in range(size + 1)]
        best_right = [[0] * (size + 1) for _ in range(size + 1)]

        for col in range(1, size):
            current = [[0] * (size + 1) for _ in range(size + 1)]

            for new_h in range(size + 1):
                for old_h in range(size + 1):

                    # current height does not exceed previous
                    if new_h <= old_h:
                        gain = prefix[col][old_h] - prefix[col][new_h]
                        current[new_h][old_h] = best_right[old_h][0] + gain

                    # current height exceeds previous
                    else:
                        gain = prefix[col - 1][new_h] - prefix[col - 1][old_h]
                        current[new_h][old_h] = max(
                            best_right[old_h][new_h],
                            best_left[old_h][new_h] + gain,
                        )

            for h1 in range(size + 1):
                rolling = current[h1][0]
                best_left[h1][0] = rolling
                for h2 in range(1, size + 1):
                    deduction = 0
                    if h2 > h1:
                        deduction = prefix[col][h2] - prefix[col][h1]

                    rolling = max(rolling, current[h1][h2] - deduction)
                    best_left[h1][h2] = rolling

                rolling = current[h1][size]
                best_right[h1][size] = rolling
                for h2 in range(size - 1, -1, -1):
                    rolling = max(rolling, current[h1][h2])
                    best_right[h1][h2] = rolling
            last_dp = current
        result = 0
        for prev_h in range(size + 1):
            result = max(result, last_dp[size][prev_h], last_dp[0][prev_h])
        return result