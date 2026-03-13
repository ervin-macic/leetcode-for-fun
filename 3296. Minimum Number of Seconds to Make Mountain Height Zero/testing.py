from math import sqrt
workerTimes = [3,2,2,4]

def contribution_until_t(t, worker_time):
    return int((sqrt(8 * t / worker_time + 1) - 1) // 2)
def total_contribution_until_t(t):
    return sum(contribution_until_t(t, worker_time) for worker_time in workerTimes)

t = 12
# worker_time = 2
# print(contribution_until_t(t, worker_time))
print(total_contribution_until_t(t))