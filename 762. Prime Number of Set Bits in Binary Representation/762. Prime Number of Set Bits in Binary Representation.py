from math import sqrt, floor
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n == 1: return False 
            for d in range(2, floor(sqrt(n)) + 1):
                if n % d == 0:
                    return False 
            return True
        cnt = 0
        for n in range(left, right+1):
            if isPrime(n.bit_count()):
                cnt += 1
        return cnt 

        