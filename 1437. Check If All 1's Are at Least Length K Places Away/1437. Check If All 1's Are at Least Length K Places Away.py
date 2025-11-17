class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        prev_one_idx = -1
        for i in range(n):
            if nums[i] == 1:
                # print(f"{prev_one_idx} and {i}")
                if prev_one_idx != -1 and i - prev_one_idx - 1 < k:
                    return False
                prev_one_idx = i 
        return True 
sol = Solution()
nums = [1,0,0,0,1,0,0,1]
k = 2
nums = [1,0,0,1,0,1]
k = 2
print(sol.kLengthApart(nums, k))

        