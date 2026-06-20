class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions.append([1, 0])
        m = len(restrictions)
        restrictions.sort()
        prev_id, prev_height = restrictions[0]
        for i in range(1, m):
            curr_id, curr_height = restrictions[i]
            restrictions[i][1] = min(curr_height, prev_height + curr_id - prev_id)
            prev_id, prev_height = restrictions[i]

        prev_id, prev_height = restrictions[-1]
        for i in range(m - 2, -1, -1):
            curr_id, curr_height = restrictions[i]
            restrictions[i][1] = min(curr_height, prev_height + prev_id - curr_id)
            prev_id, prev_height = restrictions[i]

        ans = 0
        for i in range(m - 1):
            left_id, left_height = restrictions[i]
            right_id, right_height = restrictions[i + 1]
            dist = right_id - left_id
            ans = max(ans, (left_height + right_height + dist) // 2)
        last_id, last_height = restrictions[-1]
        ans = max(ans, last_height + n - last_id)
        return ans
