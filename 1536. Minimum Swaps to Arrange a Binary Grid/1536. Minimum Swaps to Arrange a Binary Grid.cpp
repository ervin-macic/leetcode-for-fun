#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        int totalSwaps = 0;
        vector<int> rightmostOneIdx;
        for(int i = 0; i < n; i++) {
            int j = n - 1;
            while(j >= 0 && grid[i][j] == 0) j--;
            rightmostOneIdx.push_back(j);
        }

        for(int i = 0; i < n; i++) {
            int j = i;
            while(j < n && rightmostOneIdx[j] > i) {
                j++;
            }

            if(j == n) return -1;

            totalSwaps += (j - i);

            int temp = rightmostOneIdx[j];
            for(int k = j; k > i; k--) {
                rightmostOneIdx[k] = rightmostOneIdx[k - 1];
            }
            rightmostOneIdx[i] = temp;
        }

        return totalSwaps;
    }
};