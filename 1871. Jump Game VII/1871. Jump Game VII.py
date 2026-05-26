def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    if s[n-1] == '1':
        return False
    diff = [0] * (n + maxJump + 1)
    diff[minJump] = 1
    diff[maxJump + 1] = -1
    for i in range(1, n):
        diff[i] += diff[i-1]
        if diff[i] == 0:
            continue
        if s[i] == '1':
            continue
        diff[i+minJump] += 1
        diff[i+maxJump+1] -= 1
    return diff[n-1] > 0

sol = Solution()
s = "011010"
minJump = 2
maxJump = 3
print(sol.canReach(s, minJump, maxJump))