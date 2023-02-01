#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        while(l < r){
            if(numbers[l] + numbers[r] < target){
                l++;
            }else if(numbers[l] + numbers[r] > target){
                r--;
            }else{
                return {l+1, r+1};
            }
        }
        return {l+1, r+1};
    }
};
int main()
{
    Solution sol;
    vector<int> numbers{3,4,7,9,10,11,13,17,18,20};
    int target = 19;
    vector<int> ans = sol.twoSum(numbers, target);
//    cout << ans.size();
    cout << ans[0] << " " << ans[1] << endl;
}
