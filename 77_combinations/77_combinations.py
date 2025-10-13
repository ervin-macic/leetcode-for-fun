class Solution:
    def helper_combine(self, l: int, n: int, k: int) -> list[list[int]]:
        if k == 0:
            return [[]]
        if k == 1:
            ans = []
            for i in range(l, n+1):
                ans.append([i])
            return ans 
        if n-l+1 <= k:      # when there is less numbers than k, return the whole remaining range
            return [list(range(l,n+1))]
        
        ans = []
        for i in range(l, n-k+2):
            remainder = self.helper_combine(i+1, n, k-1)
            for elem in remainder:
                elem.append(i)
                ans.append(elem)
        return ans
    
    def combine(self, n: int, k: int) -> list[list[int]]:
        return self.helper_combine(1, n, k)

def main():
    sol = Solution()
    ans = sol.combine(5,2)
    print(ans)

            
main()
