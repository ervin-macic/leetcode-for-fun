import random

def reservoir_sample(stream):
    pick = None
    for i, num in enumerate(stream):
        if random.randint(0, i) == 0:
            pick = num
    return pick

nums = [5, 3, 6, 2, 7, 1, 10]
for _ in range(5):
    print(reservoir_sample(nums))
