#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    string removeStars(string s) {
        int curr_stars = 0;
        string new_s;
        for(int i = s.size()-1; i >= 0; i--) {
            if(s[i] == '*') {
                curr_stars++;
            } else {
                if(curr_stars > 0) {
                    curr_stars--;
                } else {
                    new_s.push_back(s[i]);
                }
            }
        }
        reverse(new_s.begin(), new_s.end());
        return new_s;
    }
};
int main()
{
    Solution sol;
    string s = "leet**cod*e";
    string novi = sol.removeStars(s);
    cout << novi << endl;
}
