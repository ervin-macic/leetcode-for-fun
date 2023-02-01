#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        int maxLength = 1;
        int currLength = 0;
        unordered_map<int, int> tempHash;
        while(r != s.size()){
            if(tempHash.count(s[r]) != 0){
                if(maxLength < currLength){
                    maxLength = currLength;
                }
                l = tempHash[s[r]] + 1;
                currLength = currLength - l + 1;
                tempHash.clear();
                for(int i = l; i <= r; i++) tempHash[s[i]] = i;
            }else{
                tempHash[s[r]] = r;
                currLength++;
            }
            r++;
        }
        return maxLength;
    }
};
int main()
{
    Solution sol;
    string s = "abcabcbb";
    cout << sol.lengthOfLongestSubstring(s);
}
