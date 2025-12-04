class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        # Remove L's and R's that go to infinities
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        j = n-1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # List was of form L*R*
        if i == n or j == -1 or i > j:
            return 0
        
        # Now directions[i] is first R or S
        # and directions[j] is last L or S
        ans = 0
        while i <= j:
            if directions[i] != 'S':
                ans += 1
            i += 1
        return ans
    
sol = Solution()
directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
print(sol.countCollisions(directions))