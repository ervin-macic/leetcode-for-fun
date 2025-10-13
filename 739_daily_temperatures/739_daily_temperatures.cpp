#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        int n = temperatures.size();
        stack<pair<int, int>> s;
        s.push({temperatures[0], 0});
        vector<int> ans(n);
        for(int i = 1; i < n; i++) {
                while(!s.empty() && temperatures[i] > s.top().first){
                    ans[s.top().second] = i - s.top().second;
                    s.pop();
                }
                s.push({temperatures[i], i});
            }
        return ans;
    }
};
int main(){
    vector<int> temps = {73,74,75,71,69,72,76,73};
    Solution sol = Solution();
    auto ans = sol.dailyTemperatures(temps);
    for(auto x : ans) {
        cout << x << ", ";
    }
}