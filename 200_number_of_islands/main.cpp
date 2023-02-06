#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    void floodFill(int i, int j, vector<vector<char>>& grid, int m, int n){
        if (i < 0 || j < 0 || i == m || j == n || grid[i][j] == '0' || grid[i][j] == 'X') return;
        grid[i][j]='X';
        floodFill(i+1,j,grid,m,n);
        floodFill(i,j+1,grid,m,n);
        floodFill(i-1,j,grid,m,n);
        floodFill(i,j-1,grid,m,n);
        return;

    }
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        int m = grid.size();
        int n = grid[0].size();
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    floodFill(i,j,grid,m,n);
                    //cout << i << " " << j <<endl;
                    ans++;
                }
            }
        }
        return ans;
    }
};

int main()
{
    vector<vector<char>> grid{
        {'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}
    };
//    for(int i = 0; i < grid.size(); i++){
//        for(int j = 0; j < grid[0].size(); j++){
//            cout << grid[i][j] << endl;
//        }
//    }
    Solution sol;
    cout << sol.numIslands(grid);
}
