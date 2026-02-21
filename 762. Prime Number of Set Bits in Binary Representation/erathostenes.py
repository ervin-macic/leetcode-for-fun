class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for p in range(2, int(n**0.5) + 1):
                if is_prime[p]:
                    for multiple in range(p * p, n + 1, p):
                        is_prime[multiple] = False
            return is_prime
        is_prime = sieve_of_eratosthenes(10**6)
        cnt = 0
        for n in range(left, right+1):
            if is_prime[n.bit_count()]:
                cnt += 1
        return cnt