class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stek = []
        ans = 0
        for num in nums:
            while stek and stek[-1] > num:
                stek.pop()
            if num == 0:
                continue
            else:
                if not stek:
                    # stack is empty
                    stek.append(num)
                    ans += 1
                else:
                    if stek[-1] == num:
                        # do nothing, since we can sweep consecutive ones
                        ans = ans
                    else: 
                        # stek[-1] < num case, so just append it, deal with it later
                        stek.append(num)
                        ans += 1
        return ans
    
sol = Solution()
print(sol.minOperations([3,1,2,1]))
