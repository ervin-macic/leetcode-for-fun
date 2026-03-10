from functools import lru_cache
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        n = zero + one
        @lru_cache
        def helper(remaining_zeros: int, remaining_ones: int, block_type: int, block_length: int) -> int:
            if remaining_ones == 0:
                return int(remaining_zeros <= limit)

            if remaining_zeros == 0:
                return int(remaining_ones <= limit)
                    
            # block_type 0 or 1
            assert(block_type == 0 or block_type == 1)
            if block_length < limit:
                if block_type == 0:
                    return (helper(remaining_zeros - 1, remaining_ones, 0, block_length + 1) + helper(remaining_zeros, remaining_ones - 1, 1, 1)) % MOD
                else:
                    return (helper(remaining_zeros, remaining_ones - 1, 1, block_length + 1) + helper(remaining_zeros - 1, remaining_ones, 0, 1)) % MOD
            else:
                # block_length == limit here
                if block_type == 0:
                    return helper(remaining_zeros, remaining_ones-1, 1, 1) % MOD 
                else:
                    return helper(remaining_zeros-1, remaining_ones, 0, 1) % MOD
        return (helper(zero, one-1, 1, 1) + helper(zero-1, one, 0, 1)) % MOD

sol = Solution()
# first testcase
zero = one = 3 
limit = 2
# second testcase
# zero = 1
# one = 2
# limit = 1
# expected 1 gives 2
print(sol.numberOfStableArrays(zero, one, limit))
