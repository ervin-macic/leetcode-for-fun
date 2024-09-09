#include <bits/stdc++.h>
//
using namespace std;
class Solution {
public:
    int candy(vector<int>& ratings) {
        int ans = 0;
        bool in_decreasing = false;
        int left = 0;
        vector<tuple<int, int, char>> chunks;
        ratings.push_back(ratings.back());
        for(int i = 0; i < ratings.size()-1; i++) {
            if(ratings[i] < ratings[i+1]) {
                if (in_decreasing) {
                   in_decreasing = false;
                   chunks.push_back(make_tuple(left, i, 'D'));
                   left = i+1;
                }
            } else if (ratings[i] > ratings[i+1]) {
                if (left == i) {
                    in_decreasing = true;
                } else if (!in_decreasing) {
                    chunks.push_back(make_tuple(left, i, 'I'));
                    left = i+1;
                }

            } else {
                if(in_decreasing) {
                    chunks.push_back(make_tuple(left, i, 'D'));
                } else {
                    chunks.push_back(make_tuple(left, i, 'I'));
                }
                left = i+1;
                in_decreasing = false;
            }
        }
        // ctrl k , ctrl shift x
//        for (auto tup : chunks) {
//            cout << get<2>(tup) << ": (" << get<0>(tup) << "," << get<1>(tup) << ")" << endl;
//        }

        for (int i = 0; i < chunks.size()-1; i++) {
            int l_I = get<0>(chunks[i]);
            int r_I = get<1>(chunks[i]);
            int l_D = get<0>(chunks[i+1]);
            int r_D = get<1>(chunks[i+1]);
            if ((get<2>(chunks[i]) == 'I' && get<2>(chunks[i+1]) == 'D')
                && (r_D-l_D) >= (r_I-l_I)) {
                    if(ratings[r_I] != ratings[l_D]) {
                        chunks[i] = make_tuple(l_I, r_I-1, 'I'); // r_I--;
                        chunks[i+1] = make_tuple(l_D-1, r_D, 'D'); // l_D--;
                    }
            }
        }
        for (int i = 1; i < chunks.size(); i++) {
            int l = get<0>(chunks[i]);
            int r = get<1>(chunks[i]);
            int len = r - l + 1;
            if (get<2>(chunks[i]) == 'I' && get<2>(chunks[i-1]) == 'D'
                && ratings[l] != ratings[get<1>(chunks[i-1])]) {
                ans += (len+1)*(len+2)/2 - 1;
            } else {
                ans += len*(len+1)/2;
            }
        }
        int len = get<1>(chunks[0]) - get<0>(chunks[0]) + 1;
        ans += len*(len+1)/2;
        ratings.pop_back();
        return ans;
    }

};
int main()
{
    Solution sol;
    vector<int> r = {1,6,10,8,7,3,2};
    cout << sol.candy(r) << endl;
}
