class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        prev = [1]
        ans = [prev]
        for i in range(numRows-1):
            current = [1]
            for x,y in zip(prev, prev[1:]):
                current.append(x+y)
            current.append(1)
            ans.append(current)
            prev = current 
        return ans 
sol = Solution()
print(sol.generate(5))
