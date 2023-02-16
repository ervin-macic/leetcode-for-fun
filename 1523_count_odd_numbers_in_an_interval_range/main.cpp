#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int countOdds(int low, int high) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        return ceil((high-low)/2.00) + (high%2)*(low%2);
    }
};
int main()
{
    Solution sol;
    cout << sol.countOdds(4,16);
}
