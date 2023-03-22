#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        for(int i = 0; i < haystack.size(); i++){
            if(haystack[i] == needle[0]){
                bool kill = false;
                for(int j = i; j < i + needle.size(); j++){ // 8 -> 17
                    if(haystack[j] != needle[j - i]){
                        //i = j;
                        //cout << "I'm killing this because I am at: " << j << " because: " << haystack[j] << " is not the same as " << needle[j-i] << endl;
                        kill = true;
                        break;
                    }
                }
                if(!kill){
                    return i;
                }
            }
        }
        return -1;
    }
};
int main()
{
    Solution sol;
    string needle = "issip";
    string haystack = "mississippi"; //should output 9
    cout << sol.strStr(haystack, needle) << endl;
}
