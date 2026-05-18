from collections import defaultdict, deque
class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        val_to_idx = defaultdict(list)
        for i, num in enumerate(nums):
            val_to_idx[num].append(i)
        # print(val_to_idx)
        q = deque()
        q.append(0)
        visited = [False] * n
        depth = [0] * n
        visited[0] = True
        while q:
            i = q.popleft()
            if i == n-1:
                return depth[i]
            for neighbour in val_to_idx[nums[i]]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    depth[neighbour] = depth[i] + 1
                    visited[neighbour] = True
            del val_to_idx[nums[i]]
            candidates = [i-1, i+1]
            for c in candidates:
                if 0 <= c < n and not visited[c] and c not in q:
                    q.append(c)
                    depth[c] = depth[i] + 1
                    visited[c] = True
sol = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
arr = [2,0,2,0]
print(sol.minJumps(arr))

            