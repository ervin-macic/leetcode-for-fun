#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        if(nums.size() == 1) return target == nums[0] ? 0 : -1;
        int l = 0;
        int r = nums.size() - 1;
        int mid;
        while(l <= r){
            mid = (r-l)/2 + l;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        return -1;
    }
};
int main()
{
    vector<int> nums{1};
    Solution sol;
    cout << sol.search(nums, 9);
}
