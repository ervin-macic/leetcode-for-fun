class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        ans = []
        for k in range(max(turnedOn, 4)):
            for h in range(16):
                if h < 12 and h.bit_count() == k:
                    for m in range(60):
                        if m.bit_count() == turnedOn - k:
                            if m < 10:
                                ans.append(f"{h}:0{m}")
                            else:
                                ans.append(f"{h}:{m}")
        return ans
    
turnedOn = 2
sol = Solution()
print(sol.readBinaryWatch(turnedOn))