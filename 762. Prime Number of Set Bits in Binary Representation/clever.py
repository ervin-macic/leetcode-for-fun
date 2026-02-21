class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        possible_primes = {2,3,5,7,11,13,17,19}
        cnt = 0
        for n in range(left, right+1):
            if n.bit_count() in possible_primes:
                cnt += 1
        return cnt