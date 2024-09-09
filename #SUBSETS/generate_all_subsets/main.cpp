#include <bits/stdc++.h>
using namespace std;
int main()
{
    cout << "PROGRAM TO GENERATE ALL SUBSETS OF S = {1,2,3,...,n}" << endl;
    cout << "Input n: ";
    int n;
    cin >> n;
    vector<set<int>> all_subsets;

    vector<bool> bin_str(n);
    bool all_ones = false;
    do {
        // 1 in
        set<int> temp_subset;
        for(int i = 0; i < bin_str.size(); i++)
            if(bin_str[i] == 1)
                temp_subset.insert(i+1);
        all_subsets.push_back(temp_subset);

        // INCREMENT BINARY NUMBER:
        all_ones = true;
        int idx = 0;
        while(idx != bin_str.size()){
            if(bin_str[idx] == 0) {
                bin_str[idx] = 1;
                all_ones = false;
                for(int i = idx - 1; i >= 0; i--) bin_str[i] = 0; // All ones left of idx set to 0
                break;
            } else {
                idx++;
            }
        }
    } while(!all_ones); // Go until you reach 111...111

    // PRINT ALL SUBSETS:
    cout << "{}" << endl;
    for(auto subset : all_subsets) {
        for(auto itr = subset.begin(); itr != subset.end(); itr++) {
            if(itr == subset.begin()) cout << "{";
            cout << *itr;
            if(itr != --subset.end()) cout << ",";
            else cout << "}" << endl;
        }
    }
}
