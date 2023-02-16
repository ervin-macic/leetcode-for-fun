#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool isValid(string s) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        stack<char> stek;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                stek.push(s[i]);
            }else{
                if(stek.empty()) return false;
                if(s[i] == ')' && stek.top() == '('){
                    stek.pop();
                }else if(s[i] == '}' && stek.top() == '{'){
                    stek.pop();
                }else if(s[i] == ']' && stek.top() == '['){
                    stek.pop();
                }else{
                    return false;
                }
              }
            }
            return stek.empty();
        }
};
int main()
{
    string valid = "((()[]){})";
    Solution sol;
    cout << sol.isValid(valid);
}
