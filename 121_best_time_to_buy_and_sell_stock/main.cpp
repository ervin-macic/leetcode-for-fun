#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 0;
        int maxprofit = 0;
        int profit = prices[r] - prices[l];
        // prices[l] tracks prefix min price for optimal buy
        // prices[r] just tries out everything for sell with prefix min buy price
        while(r < prices.size()){
            profit = prices[r] - prices[l];
            if(profit < 0){ //found smaller value for left bound
                l = r;
                r++;
                continue;
            }
            maxprofit = max(maxprofit, profit);
            r++;
        }
        return maxprofit;
    }
};
int main()
{
    Solution sol;
    vector<int> prices{5,1,3,4,10,8,7};
    cout << sol.maxProfit(prices) << endl;
}
