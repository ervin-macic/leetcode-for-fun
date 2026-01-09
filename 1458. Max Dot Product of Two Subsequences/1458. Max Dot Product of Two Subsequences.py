from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[-1000000 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                dp[i][j] = max(nums1[i]*nums2[j], dp[i+1][j+1] + nums1[i]*nums2[j], dp[i+1][j], dp[i][j+1])
        return dp[0][0]

sol = Solution()
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
nums1 = [-1,-1]
nums2 = [1,1,]
print(sol.maxDotProduct(nums1, nums2))
