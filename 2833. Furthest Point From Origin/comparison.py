import timeit

moves = "L_RL__R_LR__" * 1000  # make input large enough to measure

def sol1():
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

def sol2():
    l = moves.count('L')
    r = moves.count('R')
    return abs(l - r) + (len(moves) - l - r)

# run each 10,000 times
t1 = timeit.timeit(sol1, number=100)
t2 = timeit.timeit(sol2, number=100)

print("Solution 1:", t1)
print("Solution 2:", t2)