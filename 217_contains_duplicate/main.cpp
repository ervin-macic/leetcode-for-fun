#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int len = nums.size();
        unordered_map<int, bool> index;
        for(int i = 0; i < len; i++){
            if(index.find(nums[i]) == index.end()){
                index[nums[i]] = true;
            }else{
                return true;
            }
        }
        return false;
    }
};

int main()
{
    vector<int> myarr{1,2,3,4};
    Solution sol = Solution();
    cout << sol.containsDuplicate(myarr);
}
