from collections import defaultdict
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        guarded = defaultdict(bool)
        num_guarded = 0
        for guard in guards:
            x = guard[0]
            y = guard[1]
            # Check all cells north
            for i in range(x, -1, -1):
                if [i, y] in walls:
                    break
                if not guarded[(i, y)]:
                    guarded[(i, y)] = True
                    num_guarded += 1
            # Check all cells south
            for i in range(x, m):
                if [i, y] in walls:
                    break
                if not guarded[(i, y)]:
                    guarded[(i, y)] = True
                    num_guarded += 1
            # Check all cells east
            for j in range(y, n):
                if [x, j] in walls:
                    break 
                if not guarded[(x, j)]:
                    guarded[(x, j)] = True 
                    num_guarded += 1
            # Check all cells west
            for j in range(y, -1, -1):
                if [x, j] in walls:
                    break 
                if not guarded[(x, j)]:
                    guarded[(x, j)] = True 
                    num_guarded += 1
        ans = m*n - len(walls) - num_guarded
        return ans
        
sol = Solution()
m = 4 
n = 6
guards = [[0,0],[1,1],[2,3]] 
walls = [[0,1],[2,2],[1,4]]
print(sol.countUnguarded(m,n,guards,walls))