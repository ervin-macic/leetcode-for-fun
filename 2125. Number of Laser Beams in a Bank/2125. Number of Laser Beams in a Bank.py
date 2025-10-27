class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            ones = row.count('1')
            if  ones != 0:
                total += prev * ones
                prev = ones 
        return total
    
sol = Solution()
bank = ["011001","000000","010100","001000"]
bank2 = ["000","111","000"]
print(sol.numberOfBeams(bank))
        