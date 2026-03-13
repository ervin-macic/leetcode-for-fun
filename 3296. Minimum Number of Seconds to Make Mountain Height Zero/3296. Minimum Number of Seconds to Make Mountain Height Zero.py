from math import sqrt
import bisect
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        # Find contribution (in meters) of a worker until time t (in seconds)
        def contribution_until_t(t, worker_time):
            return int((sqrt(8 * t / worker_time + 1) - 1) // 2)
        def total_contribution_until_t(t):
            return sum(contribution_until_t(t, worker_time) for worker_time in workerTimes)
        l = 0
        r = 1
        # Do binary search up to find good right bound
        while total_contribution_until_t(r) < mountainHeight:
            l = r
            r *= 2
        class Wrapper:
            def __getitem__(self, i):
                return total_contribution_until_t(i)
            def __len__(self):
                return r + 1
        return bisect.bisect_left(Wrapper(), mountainHeight, lo=l, hi=r+1)

mountainHeight = 10
workerTimes = [3,2,2,4]
sol = Solution()
print(sol.minNumberOfSeconds(mountainHeight, workerTimes))
# 10 treba napravit. moze li se kako binarna po rjesenju? ako znam da ce zadnji sekund kad neko r
# (+++) (++++++) ... 
# (++) (++++) (++++++) ...
# (++) (++++) (++++++) ... 
# (++++) (++++++++) ...
# za dato vrijeme t, treba provjerit kolko smo skupili metara do tog trenutka ukljucujuci taj trenutak.
# dati radnik i ce skupit u t vremena j metara gdje je j najveci takav da workertimes[i] * (1+2+...+j) <= t.
# kad imam t kako nac j. treba mi workertimes[i] * j * (j+1) <= 2*t. rijesit kvadratnu po j? 
# j^2+j <= 2t/wt 
# 4j^2+4j+1 <= 8t/wt + 1
# 2j+1 <= sqrt(8t/wt + 1)
# j = (sqrt(8t/wt + 1) - 1) // 2
# j^2+j <= f(t) pomnozi sa 4, (2j+1)^2 <= 4f(t) + 1 uzmi sqrt i floor itd itd
# dakle mogu za svakog radnika skontat doprinos u O(1) do vremena t.
# onda samo sumirat j-ove od radnika svih i vidjet jel vise od 10.
# ovo ce bit messy binarna pretraga.