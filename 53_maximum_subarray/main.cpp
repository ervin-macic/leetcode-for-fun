#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int best = nums[0];
        int sum = nums[0];
        for(int i = 1; i < nums.size(); i++){
            // ako best[i] > 0 best[i+1] = best[i] + nums[i]
            sum = max(sum+nums[i], nums[i]);
            best = max(best, sum);
        }
        return best;
    }
};
int main()
{
    vector<int> arr{-1,2,4,-3,5,2,-5,2};
    Solution sol;
    cout << sol.maxSubArray(arr);
}
