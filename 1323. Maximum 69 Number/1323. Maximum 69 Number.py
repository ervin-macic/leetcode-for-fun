from typing import List
class Solution:
    def maximum69Number (self, num: int) -> int:
        snum = list(str(num))
        for i in range(len(snum)):
            if snum[i] == '6':
                snum[i] = '9'
                break
        ans = int("".join(snum))
        return ans
sol = Solution()
num = 9699
print(sol.maximum69Number(num))