#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    void solve(vector<vector<int>>& ans, vector<int> current_subset, vector<int> distinct, unordered_map<int, int> count, int index) {
        if(index == distinct.size()) {
            ans.push_back(current_subset);
            return;
        }
        for(int j = 0; j <= count[distinct[index]]; j++) {
            for(int k = 0; k < j; k++) {
                current_subset.push_back(distinct[index]);
            }
            solve(ans, current_subset, distinct, count, index+1);
            for(int k = 0; k < j; k++) {
                current_subset.pop_back();
            }
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        int n = nums.size();
        vector<int> distinct;
        unordered_map<int, int> count;
        for(auto num : nums) {
            if(count[num] == 0) {
                distinct.push_back(num);
            }
            count[num]++;
        }

        vector<vector<int>> ans;
        vector<int> current_subset;
        solve(ans, current_subset, distinct, count, 0);
        return ans;
    }
};
int main(){
    Solution sol;
    vector<int> nums = {1,2,2,3,3,3,5};
    auto vec = sol.subsetsWithDup(nums);
    for(auto subset : vec){
        for(auto elem : subset){
            cout << elem << " ";
        }
        cout << endl;
    }
}