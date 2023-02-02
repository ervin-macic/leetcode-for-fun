#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool isHappy(int n) {
        long long num = 0;
        int counter = 0;
        while(true){
            num = 0;
            while(n > 0){
            //cout << "NUM " << num << endl;
            num += (n % 10) * (n % 10);
            n /= 10;
            }
            //cout << num << endl;
            if(num == 4) return false;
            if(num == 1) return true;
            n = num;
            //counter++;
        }
    }
};
int main()
{
    int n = 5;
    Solution sol;
    cout << sol.isHappy(n);
}
