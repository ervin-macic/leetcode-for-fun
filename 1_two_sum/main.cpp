#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    // [1,1,3,2,5,3,4,4,7]
    // target = 10
    // (9,9,7,8,5,7,6,6,3)
    // map[1] = true
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> haveThis;
        vector<int> ans;
        for(int i = 0; i < (int)nums.size(); i++){
            if(haveThis[target - nums[i]] != 0){
                ans.push_back(i);
                ans.push_back(haveThis[target-nums[i]] - 1);
                break;
            }else{
                haveThis[nums[i]] = i + 1;
            }
        }

        return ans;
    }
};
int main()
{
    vector<int> nums{2,4,11,3};
    int target = 6;
    Solution sol;
    vector<int> answer = sol.twoSum(nums, target);
    for(auto x : answer){
        cout << x << ", ";
    }
}
