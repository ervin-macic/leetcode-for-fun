#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 0;
        int maxprofit = 0;
        int profit = prices[r] - prices[l];
        while(r < prices.size()){
            profit = prices[r] - prices[l];
            if(profit < 0){ //found smaller value for left bound
                l = r;
                r++;
                continue;
            }
            if(maxprofit < profit){
                maxprofit = profit;
            }
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
