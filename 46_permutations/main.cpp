#include <bits/stdc++.h>

using namespace std;
class Solution {
private:

    void gps(vector<int>& p, vector<int>& nums, vector<vector<int>>& answer, bool chosen[]){
    if(p.size() == nums.size()){
        answer.push_back(p);
        return ;
    }
        for(int i = 0; i < nums.size(); i++){
            if(!chosen[i]){
                p.push_back(nums[i]);
                chosen[i] = 1;
                gps(p, nums, answer, chosen);
                chosen[i] = 0;
                p.pop_back();
            }
        }
    }
public:

    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> p;
        vector<vector<int>> answer;
        bool chosen[nums.size()];
        for(int i = 0; i < nums.size(); i++) chosen[i] = false;
        generateps(p, nums, answer, chosen);
        return answer;
    }
};
int main()
{
    vector<int> nums{1,0,-1};
    Solution sol;
    vector<vector<int>> answer = sol.permute(nums);
    cout << "Now in main: " << endl;
    for(int i = 0; i < answer.size(); i++){
        for(int j = 0; j < answer[0].size(); j++){
            cout << answer[i][j] << ", ";
        }
        cout << endl;
    }
}
