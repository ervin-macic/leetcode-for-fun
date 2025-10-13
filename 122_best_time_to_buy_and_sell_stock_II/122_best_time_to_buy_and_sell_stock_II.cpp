#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        long long ans = 0;
        for(int i = 1; i < n; i++) {
            ans += max(0, prices[i]-prices[i-1]);
        }
        return ans;
    }
};
int main() {
    Solution sol = Solution();
    vector<int> prices = {7,1,5,3,6,4};
    cout << sol.maxProfit(prices) << endl;
}