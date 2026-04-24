class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        curr_neg, curr_pos = 0, 0
        for move in moves:
            if move == "R":
                curr_neg += 1
                curr_pos += 1
            elif move == "L":
                curr_neg -= 1
                curr_pos -= 1
            else:
                curr_neg -= 1
                curr_pos += 1
        return max(curr_pos, -curr_neg)

sol = Solution()
moves = "L_RL__R"
print(sol.furthestDistanceFromOrigin(moves))