class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        num_Y = 0
        num_N = 0
        best_closing_time = -1
        current_penalty = 0
        for i in range(n):
            if customers[i] == 'N':
                num_N += 1
            else:
                num_Y += 1
        
        num_N_right = num_N
        num_N_left = 0
        num_Y_right = num_Y
        num_Y_left = 0
        min_penalty = num_N_left + num_Y_right
        best_closing_time = -1
        for i in range(n):
            if customers[i] == 'N':
                num_N_left += 1
                num_N_right -= 1
            else:
                num_Y_right -= 1
                num_Y_left += 1
            
            total_penalty = num_N_left + num_Y_right
            if total_penalty < min_penalty:
                min_penalty = total_penalty
                best_closing_time = i
        return best_closing_time + 1