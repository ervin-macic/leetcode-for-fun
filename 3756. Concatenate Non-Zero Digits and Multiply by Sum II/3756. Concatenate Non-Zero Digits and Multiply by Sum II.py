MOD = 10**9 + 7
MAX_N = 100000

pow10 = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    pow10[i] = (pow10[i - 1] * 10) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        digit_sum = [0] * (n + 1)
        compressed_value = [0] * (n + 1)
        nonzero_count = [0] * (n + 1)

        for i, ch in enumerate(s):
            digit = int(ch)

            digit_sum[i + 1] = digit_sum[i] + digit
            nonzero_count[i + 1] = nonzero_count[i] + (digit != 0)

            if digit:
                compressed_value[i + 1] = (compressed_value[i] * 10 + digit) % MOD
            else:
                compressed_value[i + 1] = compressed_value[i]

        answer = []

        for left, right in queries:
            right += 1

            digits = nonzero_count[right] - nonzero_count[left]
            value = (compressed_value[right] - compressed_value[left] * pow10[digits]) % MOD
            total = digit_sum[right] - digit_sum[left]

            answer.append((value * total) % MOD)

        return answer