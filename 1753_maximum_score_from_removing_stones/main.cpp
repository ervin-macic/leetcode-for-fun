#include <iostream>

using namespace std;
class Solution {
public:
    int maximumScore(int a, int b, int c) {
        int maxi = max(a,max(b,c));
        int mini = min(a,min(b,c));
        int mid = a+b+c-maxi-mini;
        if(maxi >= mini + mid) return mini+mid;
        return (a+b+c)/2;
    }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
