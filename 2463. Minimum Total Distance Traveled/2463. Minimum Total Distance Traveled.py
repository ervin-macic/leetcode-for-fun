from typing import List
class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])

        nr = len(robot)
        nf = len(factory_positions)
        dp = [[0 for _ in range(nf+1)] for _ in range(nr+1)]

        for i in range(nr):
            dp[i][nf] = 10**10

        for i in range(nr-1, -1, -1):
            for j in range(nf-1, -1, -1):
                dp[i][j] = min(dp[i][j+1], abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1])
        return dp[0][0]  