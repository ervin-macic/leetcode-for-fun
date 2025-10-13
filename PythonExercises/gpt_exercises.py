s = set()
nums = [1, 2, 2, 3, 4, 1]
for n in nums:
    if n not in s:
        s.add(n)
    else:
        s.remove(n)
print(s)
