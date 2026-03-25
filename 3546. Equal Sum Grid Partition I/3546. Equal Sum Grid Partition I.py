class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        total = 0
        for i in range(m):
            total += sum(grid[i])
        
        if total % 2 == 1:
            return False 
        
        # vertical cut
        prefix = 0
        for j in range(n-1):
            prefix += sum(grid[i][j] for i in range(m))
            if prefix == total // 2:
                return True
        # horizontal cut 
        prefix = 0
        for i in range(m-1):
            prefix += sum(grid[i][j] for j in range(n))
            if prefix == total // 2:
                print(prefix, total)
                return True 
        return False 

sol = Solution()
grid = [[1,1,1]]
print(sol.canPartitionGrid(grid))
