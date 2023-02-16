#include <iostream>

using namespace std;
class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0){
            return 1;
        }else{
            double helper = myPow(x,n/2);
            if(n % 2 == 0){
                return helper*helper;
            }else{
                if(n > 0){
                    return x*helper*helper;
                }else{
                    return helper*helper/x;
                }
            }
        }
    }
};
int main()
{
    Solution sol;
    cout << sol.myPow(3.1415, 3);
}
