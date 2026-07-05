from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        if n == 1:
            return [1, 1]
        # dp[i][j] is max length path from (i,j) to E
        dp = [[-float("inf") for _ in range(n)] for _ in range(n)]
        p = [[[] for _ in range(n)] for _ in range(n)]
        dp[0][0] = 0
        # first row
        j = 1
        while j < n and board[0][j] != 'X' and board[0][j] != 'S':
            dp[0][j] = dp[0][j-1] + int(board[0][j])
            p[0][j].append((0, j-1))
            j += 1
        # first col
        i = 1
        while i < n and board[i][0] != 'X' and board[i][0] != 'S':
            dp[i][0] = dp[i-1][0] + int(board[i][0])
            p[i][0].append((i-1, 0))
            i += 1
        # remaining
        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] != 'X' and board[i][j] != 'S':
                    candidates = [(i-1, j), (i-1, j-1), (i, j-1)]
                    # find dp[i][j]
                    for ni, nj in candidates:
                        if board[ni][nj] != 'X':
                            dp[i][j] = max(dp[i][j], dp[ni][nj] + int(board[i][j]))
                    # save parents
                    for ni, nj in candidates:
                        if board[ni][nj] != 'X':
                            if dp[ni][nj] + int(board[i][j]) == dp[i][j]:
                                p[i][j].append((ni, nj))
        maxLen = dp[n-1][n-1] = max(dp[n-2][n-1], dp[n-2][n-2], dp[n-1][n-2])
        # now count paths
        count = [[0 for _ in range(n)] for _ in range(n)]
        count[0][0] = 1
        # first row
        j = 1
        while j < n and board[0][j] != 'X' and board[0][j] != 'S' and (0, j-1) in p[0][j]:
            count[0][j] = count[0][j-1]
            j += 1
        # first col
        i = 1
        while i < n and board[i][0] != 'X' and board[i][0] != 'S' and (i-1, 0) in p[i][0]:
            count[i][0] = count[i-1][0]
            i += 1
        # remaining 
        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] != 'X' and board[i][j] != 'S':
                    candidates = [(i-1, j), (i-1, j-1), (i, j-1)]
                    for ni, nj in candidates:
                        if board[ni][nj] != 'X' and (ni, nj) in p[i][j]:
                            count[i][j] += count[ni][nj]
        if maxLen == -float("inf"):
            return [0, 0]
        # for i in range(n):
        #     for j in range(n):
        #         print(f"{i,j} parent: {p[i][j]}")
        # print(dp, count)
        totalCount = 0
        candidates = [(n-2, n-1), (n-1, n-2), (n-2, n-2)]
        for ni, nj in candidates:
            if dp[ni][nj] == maxLen:
                totalCount += count[ni][nj]
        return [maxLen, totalCount % (10**9+7)]
sol = Solution()
board = ["E12",
         "1X1",
         "21S"]
board = ["E23",
         "2X2",
         "12S"]
print(sol.pathsWithMaxScore(board))