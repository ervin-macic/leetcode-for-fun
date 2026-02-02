from sortedcontainers import SortedList
from typing import List 
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ans = nums[0]
        # Keep sorted window [i,...i+dist]
        sl = SortedList(nums[1:dist+2])
        cum_sum = sum(sl[:k-1])
        # Initialize ans as the solution if i1 = 1
        ans += cum_sum
        n = len(nums)
        # Check whether it's better to have i1 = i for each i in {2,3,..n-k+1}
        for i in range(2, n-k+2):
            if sl.index(nums[i-1]) < k - 1:
                cum_sum -= nums[i-1]
                if len(sl) > k-1:
                    cum_sum += sl[k-1]
            sl.remove(nums[i-1])
            if i+dist < n:
                sl.add(nums[i+dist])
                if sl.index(nums[i+dist]) < k - 1:
                    cum_sum += nums[i+dist]
                    if len(sl) > k-1:
                        cum_sum -= sl[k-1]
            ans = min(ans, nums[0] + cum_sum)
        return ans

sol = Solution()
nums = [1,3,2,6,4,2]
k = 3
dist = 3
nums = [2,6,3,8,3,1,1]
k =3 
dist =4
print(sol.minimumCost(nums, k, dist))

        
