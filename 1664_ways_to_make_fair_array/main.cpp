#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int waysToMakeFair(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return 1;
        int ans = 0;
        vector<int> odd_sums(n/2+1, 0);
        vector<int> even_sums(n/2+1, 0);
        int even_sum = 0;
        int odd_sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(i % 2 == 0) {
                even_sum += nums[i];
            } else {
                odd_sum += nums[i];
            }
        }
        if(even_sum - nums[0] == odd_sum) {
            ans++;
        }
        if(n%2 == 0) {
            if(odd_sum - nums.back() == even_sum){
                ans++;
            }
        } else {
            if(even_sum - nums.back() == odd_sum){
                ans++;
            }
        }

        int cum_odd = 0;
        int cum_even = 0;
        int new_even = 0;
        int new_odd = 0;
        cum_even = nums[0];

        for(int i = 1; i < nums.size()-1; i++) {
            if(i % 2 == 0) {
                cum_even += nums[i];
                new_even = (odd_sum-cum_odd) + (cum_even-nums[i]);
                new_odd = (even_sum-cum_even) + cum_odd;
            } else {
                cum_odd += nums[i];
                new_even = (odd_sum-cum_odd) + cum_even;
                new_odd = (even_sum-cum_even) + (cum_odd-nums[i]);
            }
            if(new_even == new_odd) ans++;
        }
        return ans;
    }
};
int main()
{
    Solution sol;
    vector<int> test = {1,1,1,1,1};
    cout << sol.waysToMakeFair(test);
}
