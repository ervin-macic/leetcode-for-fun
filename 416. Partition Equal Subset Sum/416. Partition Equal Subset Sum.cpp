#include<algorithm>
#include<vector>
#include<numeric>
#include<bitset>
using namespace std;
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int S = accumulate(nums.begin(), nums.end(), 0);
        if(S % 2 == 1) return false; 
        bitset<20001> dp;
        dp[0] = 1;
        for(auto num : nums) {
            dp = dp | (dp << num);
        }
        return dp[S/2];
    }
};
        
