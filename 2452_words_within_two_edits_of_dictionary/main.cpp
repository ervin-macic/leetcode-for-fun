#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> collection;
        int dif;
        for(auto query : queries) {
            for(auto dict : dictionary) {
                dif = 0;
                for(int i = 0; i < dict.size(); i++) {
                    if(query[i] != dict[i]) {
                        dif++;
                    }
                    if(dif > 2) break;
                }
                if(dif <= 2) {
                    collection.push_back(query);
                    break;
                }
            }
        }
        return collection;
    }
};
int main()
{
    Solution sol;
    vector<string> queries = {"word","note","ants","wood"};
    vector<string> dictionary = {"wood","joke","moat"};
    auto vec = sol.twoEditWords(queries, dictionary);
    for (auto x : vec) cout << x << endl;
}
