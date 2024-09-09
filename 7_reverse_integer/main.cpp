#include <bits/stdc++.h>

using namespace std;
// [-2^31, 2^31 - 1] 32-bit signed integer

class Solution {
public:
    int reverse(int x) {
        if(x == 0) return 0;
        int reversed_x = 0;
        bool is_negative = (x < 0) ? true : false;
        int temp_x = x;
        int exp10 = 1;
        int br = 0;
        while(temp_x != 0){
            temp_x /= 10;
            if(br != 0) {
                if(exp10 > INT_MAX / 10) return 0;
                exp10 *= 10;
            }
            br = 1;
        }
        if(is_negative && x != INT_MIN) x *= -1;
        if(x == INT_MIN) return 0;
        while(x != 0) {
            if(x%10 != 0 && exp10 > INT_MAX / (x%10)) return 0;
            if(is_negative && (reversed_x-1) > INT_MAX - (x%10)*exp10) return 0;
            if(!is_negative && (reversed_x) > INT_MAX - (x%10)*exp10) return 0;
            reversed_x += (x%10) * exp10;
            exp10 /= 10;
            x /= 10;
        }
        if(is_negative) reversed_x *= -1;
        return reversed_x;
    }
};
int main()
{
    Solution sol;
    cout << sol.reverse(-2147483648);
}
