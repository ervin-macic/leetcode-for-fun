class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            c = Counter(nums[i:i+k])
            c = sorted(c.items(), key=lambda a: (-a[1], -a[0]))
            best_sum = sum(v for v in nums[i:i+k] if v in set(v for v, _ in c[:x]))
            ans.append(best_sum)

        return ans





sol = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
ans = sol.findXSum(nums, k, x)
for elem in ans:
   print(elem)