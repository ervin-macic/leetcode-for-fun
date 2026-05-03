#include <iostream>
using namespace std;
class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.length() != goal.length()) return False;
        size_t n = s.size();
        for (size_t start = 0; start < n; ++start) {
            if(s[start] != goal[start]) continue;
            int i = 0;
            while(i < n and s[(start + i) % n] == goal[i]) i += 1
            if i == n:
                return true;
        }
        return false;
    }
};
int main() {
    
}