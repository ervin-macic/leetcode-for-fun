from collections import defaultdict

def main():
    nums = [1,4,2,3,4,9,3]
    target = 13
    remainders = defaultdict(lambda: -1)
    for i in range(len(nums)):
        j = remainders[nums[i]]
        if j != -1:
            print(f"Solution: ({j}, {i})")
        else:
            remainders[target-nums[i]] = i
main()