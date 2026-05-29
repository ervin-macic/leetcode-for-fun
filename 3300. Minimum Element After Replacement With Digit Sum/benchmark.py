import timeit

# 1. The original math approach
def digit_sum_math(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

# 2. The optimized string approach
def digit_sum_string_map(num):
    return sum(map(int, str(num)))


# Test cases to evaluate scaling
test_cases = {
    "Small Number (3 digits)": 123,
    "Medium Number (9 digits)": 123456789,
    "Large Number (30 digits)": 123456789012345678901234567890
}

number_of_runs = 100_000

print(f"Running each function {number_of_runs:,} times per test case:\n")
print(f"{'Test Case':<30} | {'Math Time (s)':<15} | {'String/Map Time (s)':<20} | {'Winner'}")
print("-" * 78)

for name, num in test_cases.items():
    # Measure execution time
    math_time = timeit.timeit(lambda: digit_sum_math(num), number=number_of_runs)
    string_time = timeit.timeit(lambda: digit_sum_string_map(num), number=number_of_runs)
    
    # Determine the winner
    winner = "Math" if math_time < string_time else "String/Map"
    margin = max(math_time, string_time) / min(math_time, string_time)
    
    print(f"{name:<30} | {math_time:<15.4f} | {string_time:<20.4f} | {winner} ({margin:.1f}x faster)")