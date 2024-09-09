#include <bits/stdc++.h>

using namespace std;
// 1 3 5 4 2 => 1 4 2 3 5
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool is_max_perm = true;
        for(int i = nums.size() - 1; i > 0; i--) {
            if(nums[i] > nums[i-1]) {
                int best_idx = i;
                for(int j = i+1; j < nums.size(); j++) {
                    if(nums[j] > nums[i-1] && nums[j] < nums[best_idx]) {
                      best_idx = j;
                    }
                }
                iter_swap(nums.begin()+i-1, nums.begin()+best_idx);
                sort(nums.begin()+i, nums.end());
                is_max_perm = false;
                break;
            }
        }
        if(is_max_perm) {
            reverse(nums.begin(), nums.end());
        }
    }
};
int main()
{
    Solution sol;
    vector<int> vec = {2,1,2,2,2,2,2,1};
    sol.nextPermutation(vec);
    for(auto x : vec) cout << x << endl;
    return 0;
}
