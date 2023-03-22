#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) return false;
        if(x == 0) return true;
        if(x%10 == 0) return false;
        int x_reversed = 0;
        while(x > x_reversed){
            x_reversed = x_reversed*10 + x%10;
            x /= 10;
        }
        cout << x << " " << x_reversed;
        if(x == x_reversed / 10 || x == x_reversed) return true; //14241   x_reeversed: 1 x = 1424 (14, 142) (142, 14)
        return false;
    }
};
int main()
{
    Solution sol;
    cout << sol.isPalindrome(12321);
}
