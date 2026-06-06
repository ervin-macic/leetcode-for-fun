class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return self._count_up_to(num2 + 1) - self._count_up_to(num1)


    def _count_up_to(self, limit: int) -> int:
        ans = 0

        higher = limit // 10
        suffix = limit % 10
        place = 1

        while higher >= 10:
            cur = higher % 10
            left_neighbor = (higher // 10) % 10
            right_neighbor = suffix // place

            higher //= 10

            if cur > left_neighbor:
                greater_pairs = cur * (cur - 1) // 2
                blocked_pairs = left_neighbor * (left_neighbor + 1) // 2

                ans += (greater_pairs - blocked_pairs) * place

                if cur > right_neighbor:
                    ans += suffix
                else:
                    ans += cur * place

            elif cur < left_neighbor and cur < right_neighbor:
                ans += suffix - (cur + 1) * place

            gap = 9 - min(cur, left_neighbor)

            poly = (
                left_neighbor
                * (121 + 15 * left_neighbor - left_neighbor * left_neighbor)
                // 3
            )

            ans += (
                570 * (higher // 10)
                + poly
                - gap * (gap + 1) // 2
            ) * place

            place *= 10
            suffix += cur * place

        return ans