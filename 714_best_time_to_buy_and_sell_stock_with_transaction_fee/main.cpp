#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        long long int dp_nothing_held = 0, dp_stock_held = INT_MIN;

        for (int i = 0; i < prices.size(); i++) {
            long long int dp_nothing_held_prev = dp_nothing_held;
            dp_nothing_held = max(dp_nothing_held, dp_stock_held + prices[i] - fee);
            dp_stock_held = max(dp_stock_held, dp_nothing_held_prev - prices[i]);
        }

        return dp_nothing_held;
    }
};
int main()
{
    Solution sol;
    vector<int> prices = {1,3,7,5,10,3};
    cout << sol.maxProfit(prices, 3) << endl;
}
