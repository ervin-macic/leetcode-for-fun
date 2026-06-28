class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]
sol = Solution()
arr = [73,98,9]
print(sol.maximumElementAfterDecrementingAndRearranging(arr))