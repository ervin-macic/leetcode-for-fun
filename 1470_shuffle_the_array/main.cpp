#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        for(int i = 0; i < n; i++){
            nums[i] = nums[i]<<10;
            nums[i] = nums[i]|nums[n+i];
        }
        /*for(int i = 0; i < n; i++){
            cout << nums[i] << endl;
        }*/
        for(int i = 0; i < n; i++){
            nums[2*n-1-2*i] = nums[n-1-i]&(1023);
            nums[2*n-2-2*i] = nums[n-1-i]>>10;
        }
        return nums;
    }
};
int main()
{
    vector<int> etwa{1,4,5,6,7,12,32,30};
    Solution sol;
    vector<int> nums = sol.shuffle(etwa,4);
    for(auto x : nums) cout << x << endl;
}
