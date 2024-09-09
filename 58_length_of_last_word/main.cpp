#include <iostream>

using namespace std;
class Solution {
public:
    int lengthOfLastWord(string s) {
        int ptr1 = s.size() - 1;
        int ptr2 = s.size() - 1;
        while(s[ptr1] == ' ') ptr1--;
        ptr2 = ptr1+1;
        while(ptr1 >= 0 && s[ptr1] != ' ') ptr1--;
        ptr1++;
        return ptr2 - ptr1;
    }
};
int main()
{
    Solution sol;
    cout << sol.lengthOfLastWord(" asd hee d");
}
