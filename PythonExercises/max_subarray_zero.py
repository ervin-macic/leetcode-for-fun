def longest_zero_sum_subarray(nums: list):
    prefix_sum = 0
    max_len = 0
    max_l = -1 
    max_r = -1
    seen = {0 : -1} # keep prefix_sum -> index where we achieved it
    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
            max_l = seen[prefix_sum]
            max_r = i
        else:
            seen[prefix_sum] = i 
    
    return max_len, max_l, max_r

def main():
    nums = [1,-2,3,5,10,-12,-3,-1]
    print(longest_zero_sum_subarray(nums))

main()