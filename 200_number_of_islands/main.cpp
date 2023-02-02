#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    void floodFill(int i, int j, vector<vector<char>>& grid){
        //cout << i << " " << j << endl;
        if(j - 1 >= 0 and grid[i][j-1] == '1'){
            grid[i][j-1] = 'X';
            floodFill(i,j-1,grid);
        }
        if(i - 1 >= 0 and grid[i-1][j] == '1'){
            grid[i-1][j] = 'X';
            floodFill(i-1,j,grid);
        }
        if(i + 1 < (int)grid[0].size() and grid[i+1][j] == '1'){
            grid[i+1][j] = 'X';
            floodFill(i+1,j,grid);
        }
        if(j + 1 < (int)grid.size() and grid[i][j+1] == '1'){
            grid[i][j+1] = 'X';
            floodFill(i,j+1,grid);
        }
        //cout << "fuck";
    }
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == '1'){
                    grid[i][j] = 'X';
                    floodFill(i,j,grid);
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
