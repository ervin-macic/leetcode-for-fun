#include <iostream>

using namespace std;
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> hash;
        int l = 0;
        int r = 0;
        while(r < fruits.size()) {
            hash[fruits[r]]++;
            if (hash.size() > 2) {
                hash[fruits[l]]--;
                if (hash[fruits[l]] == 0){
                    hash.erase(fruits[l]);
                }
                l++;
            }
            r++;
        }
        return r - l;
    }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
