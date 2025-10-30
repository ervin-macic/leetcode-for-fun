#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int helper(const vector<int>& target, int l, int r, int damage) {
        if (l > r) return 0;
        if (l == r) return target[l] - damage;

        int curr_min = 1e9;
        int curr_min_idx = -1;
        for (int i = l; i <= r; ++i) {
            if (target[i] - damage < curr_min) {
                curr_min = target[i] - damage;
                curr_min_idx = i;
            }
        }

        return helper(target, l, curr_min_idx - 1, curr_min + damage)
            + helper(target, curr_min_idx + 1, r, curr_min + damage)
            + curr_min;
    }
    int minNumberOperations(vector<int>& target) {
        int curr_min = 1e9;
        int curr_min_idx = -1;
        for (int i = 0; i < target.size(); i++) {
            if (target[i] < curr_min) {
                curr_min = target[i];
                curr_min_idx = i;
            }
        }

        return helper(target, 0, curr_min_idx - 1, curr_min)
            + helper(target, curr_min_idx + 1, target.size(), curr_min)
            + curr_min;
    }
};

int main(){
    vector<int> ex1{3,1,5,4,2};
    
    Solution sol = Solution();
    cout << sol.minNumberOperations(ex1);
}