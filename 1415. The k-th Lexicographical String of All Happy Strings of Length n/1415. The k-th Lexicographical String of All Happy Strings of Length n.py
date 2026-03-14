class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        pow2 = 2 ** (n-1)
        if k > 3 * pow2:
            return ""
        chars = []
        d = {0 : 'a', 
             1 : 'b', 
             2 : 'c'}
        def helper(m, k, prev_char):
            if m == 0:
                return
            pow2 = 2 ** (m-1)
            lst = ['a', 'b', 'c']
            lst.remove(prev_char)
            if k > pow2:
                chars.append(lst[1])
                k -= pow2 
                helper(m-1,k,lst[1])
            else:
                chars.append(lst[0])
                helper(m-1,k,lst[0])
        i = 0
        while k > pow2:
            k -= pow2 
            i += 1
        chars.append(d[i])
        helper(n-1, k, d[i])
        return "".join(chars)
n = 3 
k = 9
sol = Solution()
print(sol.getHappyString(n,k))

# n = 3, k = 9 here should return cab
# n = 1 has 3 happy strings [a, b, c]
# n = 2 has 6 happy strings [ab, ac, ba, bc, ca, cb]
# n = 3 has 12 happy strings ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]
# n = 4 has 24 happy strings (8 with a first, 8 with b first, 8 with c first) [abab, abac, abca, abcb, acab.., baba, babc, baca, bacb, b]
# n = 5 has 48 happy strings (so x2 each time, has segments of length 16 = 2^4)
# in general n has 3*2^(n-1) happy strings with segments of length 2^(n-1)
# just need to check in which segment k is located. then once that is done, calculate new adjusted k' by subtracting off i*2^(n-1) where i = 0,1 or 2
# and solve the new problem for n-1
