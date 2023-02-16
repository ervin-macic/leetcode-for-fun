#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    vector<int> ans;
    int x = 0;
    int y = 0;
    void right(int i, int j, int dist, vector<vector<int>> matrix){
        int limit = j + dist;
        j++;
        for(; j < limit; j++){
            ans.push_back(matrix[i][j]);
        }
        x = i;
        y = j - 1;
    }
    void down(int i, int j, int dist, vector<vector<int>> matrix){
        int limit = i + dist;
        i++;
        for(; i < limit; i++){
            ans.push_back(matrix[i][j]);
        }
        x = i - 1;
        y = j;
    }
    void left(int i, int j, int dist, vector<vector<int>> matrix){
        int limit = j - dist + 1;
        j--;
        for(; j >= limit; j--){
            ans.push_back(matrix[i][j]);
        }
        x = i;
        y = j + 1;
    }
    void up(int i, int j, int dist, vector<vector<int>> matrix){
        int limit = i - dist + 1;
        i--;
        for(; i >= limit; i--){
            ans.push_back(matrix[i][j]);
        }
        x = i + 1;
        y = j;
    }
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        ans.push_back(matrix[0][0]);
        int cnt = 0;
        if(n == 1){
           down(0,0,m,matrix);
           return ans;
        }
        if(m == 1){
            right(0,0,n,matrix);
            return ans;
        }
        while(m > 0 and n > 0){
            if(cnt == 1) n++;
            if(cnt % 4 == 0){
                right(x, y, n, matrix);
                n--;
            }else if(cnt % 4 == 1){
                down(x, y, m, matrix);
                m--;
            }else if(cnt % 4 == 2){
                left(x, y, n, matrix);
                n--;
            }else{
                up(x, y, m, matrix);
                m--;
            }
            cnt++;
        }
        return ans;
    }
};
int main()
{
    Solution sol;
    vector<vector<int>> matrix{{3}};
    //vector<vector<int>> matrix{{1,2,3,4,5,6},{7,8,9,10,11,12},{13,14,15,16,17,18},{19,20,21,22,23,24}};
    vector<int> ans = sol.spiralOrder(matrix);
    for(auto x : ans){
        cout << x << " ";
    }
}
