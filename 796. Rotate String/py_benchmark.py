# =========================
# PYTHON BENCHMARK SUITE
# =========================
import timeit
import random
import string

def rotate_find(s, goal):
    if len(s) != len(goal):
        return False
    return (s + s).find(goal) != -1

def rotate_manual(s, goal):
    n = len(s)
    if n != len(goal):
        return False

    for start in range(n):
        if s[start] != goal[0]:
            continue

        i = 0
        while i < n and s[(start + i) % n] == goal[i]:
            i += 1

        if i == n:
            return True

    return False


# -------------------------
# Helpers
# -------------------------
def rotate_by_k(s, k):
    k %= len(s)
    return s[k:] + s[:k]

def random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


# -------------------------
# Test Cases
# -------------------------
tests = []

# Small strings
tests.append(("abcde", "cdeab", "small_true"))
tests.append(("abcde", "abced", "small_false"))

# Medium strings
s = "abcdefg" * 1000
tests.append((s, rotate_by_k(s, 300), "medium_true"))
tests.append((s, s[::-1], "medium_false"))

# Repetitive strings
s = "a" * 5000 + "b"
tests.append((s, rotate_by_k(s, 2000), "repeat_true"))
tests.append((s, "a" * len(s), "repeat_false"))

# Random strings
s = random_string(10000)
tests.append((s, rotate_by_k(s, 4321), "random_true"))

g = random_string(10000)
tests.append((s, g, "random_false"))

# Large strings
s = "xyz12345" * 20000
tests.append((s, rotate_by_k(s, 7777), "large_true"))
tests.append((s, s[:-1] + "Q", "large_false"))


# -------------------------
# Run Benchmark
# -------------------------
for s, goal, name in tests:
    assert rotate_find(s, goal) == rotate_manual(s, goal)

    t1 = timeit.timeit(lambda: rotate_find(s, goal), number=200)
    t2 = timeit.timeit(lambda: rotate_manual(s, goal), number=200)

    print(f"{name:15} | find={t1:.6f}s | manual={t2:.6f}s | x{t2/t1:.2f}")