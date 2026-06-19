class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr = 0 
        ans = 0
        for g in gain:
            curr += g
            ans = max(ans, curr)
        return ans
lst = [-4,-3,-2,-1,4,3,2]
print(list(accumulate(lst)))