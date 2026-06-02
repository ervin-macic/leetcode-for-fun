class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans, min_f_land, min_f_water = 2001, 2001, 2001

        # get min_f_land 
        for s_land, d_land in zip(landStartTime, landDuration):
            min_f_land = min(min_f_land, s_land + d_land)

        # get min_f_water
        for s_water, d_water in zip(waterStartTime, waterDuration):
            min_f_water = min(min_f_water, s_water + d_water)
        
        # check first land second water
        for s_water, d_water in zip(waterStartTime, waterDuration):
            ans = min(ans, max(min_f_land, s_water) + d_water)

        # check first water second land 
        for s_land, d_land in zip(landStartTime, landDuration):
            ans = min(ans, max(min_f_water, s_land) + d_land)

        return ans