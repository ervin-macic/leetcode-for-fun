#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        int maxLength = 0;
        int currLength = 0;
        unordered_map<int, int> tempHash;
        while(r != s.size()){
            cout << l << " " << r << " " << currLength << endl;
            if(maxLength < currLength){
                maxLength = currLength;
            }
            if(tempHash.count(s[r]) != 0){
                cout << "problem: " << tempHash[s[r]] << endl;
                    currLength = r - tempHash[s[r]];
                while(l <= tempHash[s[r]]){
                    tempHash.erase(s[l]);
                    l++;
                }
            }else{
                currLength++;
                if(maxLength < currLength){
                maxLength = currLength;
                }
            }
            tempHash[s[r]] = r;
            r++;

        }
        return maxLength;
    }
};
int main()
{
    Solution sol;
    string s = " ";
    cout << sol.lengthOfLongestSubstring(s);
}
