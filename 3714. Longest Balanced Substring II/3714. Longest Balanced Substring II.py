from collections import defaultdict
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        # 1st case - just a's or just b's or just c's
        max_1st_case = -float("inf")
        for a in ['a', 'b', 'c']:
            As = 0
            for i in range(n):
                if s[i] == a:
                    As += 1
                    max_1st_case = max(max_1st_case, As)
                else:
                    As = 0
        
        # 2nd case - (a,b) (b,c) (c,a)
        max_2nd_case = -float("inf")
        for (a,b) in [('a','b'), ('b','c'), ('c','a')]:
                As = Bs = Cs = 0
                pairs = set()
                pairs.add((0,0))
                pair_to_idx = defaultdict(int)
                pair_to_idx[(0,0)] = -1
                for j in range(n):
                    if s[j] == a:
                        As += 1
                    elif s[j] == b:
                        Bs += 1
                    else:
                        Cs += 1
                    p = (As - Bs, Cs)
                    if p in pairs:
                        i = pair_to_idx[p]
                        max_2nd_case = max(max_2nd_case, j-i)
                    else:
                        pairs.add(p)
                        pair_to_idx[p] = j
        
        # 3rd case - (a,b,c)
        As = Bs = Cs = 0
        pairs = set()
        pairs.add((0,0))
        pair_to_idx = defaultdict(int)
        pair_to_idx[(0,0)] = -1
        max_3rd_case = -float("inf")
        for j in range(n):
            if s[j] == 'a':
                As += 1
            elif s[j] == 'b':
                Bs += 1
            else:
                Cs += 1
            p = (As - Bs, As - Cs)
            if p in pairs:
                i = pair_to_idx[p]
                max_3rd_case = max(max_3rd_case, j-i)
            else:
                pairs.add(p)
                pair_to_idx[p] = j 
        return max(max_1st_case, max_2nd_case, max_3rd_case)

sol = Solution()
s = "ccaca"
print(sol.longestBalanced(s))