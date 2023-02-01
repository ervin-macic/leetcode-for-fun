#include <bits/stdc++.h>

using namespace std;
const static auto fast = []
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> countCharS;
        unordered_map<char, int> countCharT;

        if(s.length() != t.length()) return false;

        for(int i = 0; i < (int)s.length(); i++){
            countCharS[s[i]]++;
            countCharT[t[i]]++;
        }
        return (countCharS == countCharT);

    }
};
int main()
{
    string s = "anaramg";
    string t = "granaam";
    Solution sol;
    cout << sol.isAnagram(s,t) << endl;
}
