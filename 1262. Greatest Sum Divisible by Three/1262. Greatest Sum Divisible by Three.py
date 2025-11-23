class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] % 3 == 0:
                return nums[0]
            else:
                return 0
        else:
            s = 0
            CONST = 10**5
            min_1_mod_3 = CONST
            second_min_1_mod_3 = CONST
            min_2_mod_3 = CONST
            second_min_2_mod_3 = CONST
            for i in range(n):
                s += nums[i]
                if nums[i] % 3 == 2:
                    if nums[i] < min_2_mod_3:
                        if min_2_mod_3 != CONST:
                            second_min_2_mod_3 = min_2_mod_3
                        min_2_mod_3 = nums[i]
                    elif nums[i] < second_min_2_mod_3:
                        second_min_2_mod_3 = nums[i]
                if nums[i] % 3 == 1:
                    if nums[i] < min_1_mod_3:
                        if min_1_mod_3 != CONST:
                            second_min_1_mod_3 = min_1_mod_3
                        min_1_mod_3 = nums[i]
                    elif nums[i] < second_min_1_mod_3:
                        second_min_1_mod_3 = nums[i]
                    
            # print(f"min_1_mod_3: {min_1_mod_3}, second_min_1_mod_3: {second_min_1_mod_3}, min_2_mod_3: {min_2_mod_3}, second_min_2_mod_3: {second_min_2_mod_3}")
            if s % 3 == 0:
                return s
            elif s % 3 == 1:
                if min_1_mod_3 != CONST:
                    if second_min_2_mod_3 != CONST:
                        return max(s-min_1_mod_3, s-min_2_mod_3-second_min_2_mod_3)
                    else:
                        return s-min_1_mod_3
                else:
                    return (s-min_2_mod_3-second_min_2_mod_3)
            else:
                if min_2_mod_3 != CONST:
                    if second_min_1_mod_3 != CONST:
                        return max(s-min_2_mod_3, s-min_1_mod_3-second_min_1_mod_3)
                    else:
                        return s-min_2_mod_3
                else:
                    return s-min_1_mod_3-second_min_1_mod_3



sol = Solution()
nums = [3,6,5,1,8]
print(sol.maxSumDivThree(nums))