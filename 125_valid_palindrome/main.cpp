#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> newS;
        bool answer = false;
        for(int i = 0; i < (int)s.length(); i++){
            if(iswalnum(s[i])){
                newS.push_back(tolower(s[i]));
            }
        }
        int len = newS.size();
        for(int i = 0; i < len; i++){
            if(newS[i] != newS[len - i - 1]) return false;
        }
        return true;
    }
};
int main()
{
    Solution sol;
    string s = "ana voli, millovana?";
    cout << sol.isPalindrome(s) << endl;
}
