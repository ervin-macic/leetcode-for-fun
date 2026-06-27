class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                nums[i] = 1
            else:
                nums[i] = -1
        pref = [0] * (n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1] + nums[i]
        
