#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int get_index(int n, int i, int j) {
        if(i % 2 == 0) {
            return (n * n - n * i - (j));
        } else {
            return (n * n - n * i - (n - 1- j));
        }
    }
    pair<int, int> get_i_j(int n, int idx) {
        int i = (n - 1) - ((idx - 1) / n);
        int j;
        if (i % 2 == 0) {
            j = (n - 1) - idx + n * (n - 1 - i) + 1;
        } else {
            j = idx - n * (n - 1 - i) - 1;
        }
        return make_pair(i, j);
    }
    void print_pq(auto pq) {
        cout << " P R I N T A M P Q " << endl;
        while(!pq.empty()) {
            cout << pq.top() << " ";
            pq.pop();
        }
        cout << endl;
        cout << "Z A V R S I O P R I N T A N J E P Q" << endl;
        cout << endl;
    }
    int prev_six_min(auto board, int i, int j) {
        if(j > 6) {
            return min()
        }
    }
    int snakesAndLadders(vector<vector<int>>& board) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        // dp-asto
        int n = board.size();
        int dp[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                dp[i][j] = INT_MAX;
            }
        }
        dp[n-1][0] = 0;
        priority_queue<int, vector<int>, greater<int>> prev_six;
        // for (int i = 0; i < 6; i++) prev_six.push(0);
        for (int i = n-1; i >= 0; i--) {
            if(i % 2 == 0) {
                for (int j = n-1; j >= 0; j--) {
                    print_pq(prev_six);
                    // right to left
                    if (board[i][j] == -1) {
                        dp[i][j] = min(dp[i][j], prev_six.top()+1);
                    } else {
                        cout << "POLJE: (" << i << "," << j << ") ima vrijednost: " << board[i][j] << endl;
                        dp[i][j] = min(dp[i][j], prev_six.top()+1);
                        pair<int, int> indices = get_i_j(n, board[i][j]);
                        cout << "SALJE ME NA INDEKSE: " << indices.first << " i " << indices.second << endl;
                        int I = indices.first;
                        int J = indices.second;
                        if((I == i and J > j) or (I > i)) { // snake
                            cout << "OVO JE ZMIJA" << endl;
                            int temp = dp[I][J];
                            dp[I][J] = min(dp[i][j], dp[I][J]);
                            if(temp > dp[I][J]) {
                                i = I;
                                j = J;
                            }
                        } else { // ladder
                            cout << "OVO JE LJESTVA" << endl;
                            dp[I][J] = min(dp[I][J], dp[i][j]);
                        }
                    }
                    prev_six.push(prev_six.top()+1);
                    prev_six.pop();
                    
                    cout << "DP TABLE: " << endl;
                    for(int i = 0; i < n; i++) {
                        for(int j = 0; j < n; j++) {
                            cout << dp[i][j] << " ";
                        }
                        cout << endl;
                    }
                    cout << "DONE WITH DP TABLE" << endl;
                }
            } else {
                for (int j = 0; j < n; j++) {
                    print_pq(prev_six);
                    // left to right
                    if (board[i][j] == -1) {
                        dp[i][j] = min(dp[i][j], prev_six.top()+1);
                    } else {
                        cout << "POLJE: (" << i << "," << j << ") ima vrijednost: " << board[i][j] << endl;
                        dp[i][j] = min(dp[i][j], prev_six.top()+1);
                        pair<int, int> indices = get_i_j(n, board[i][j]);
                        cout << "SALJE ME NA INDEKSE: " << indices.first << " i " << indices.second << endl;
                        int I = indices.first;
                        int J = indices.second;
                        if((I == i and J < j) or (I > i)) { // snake
                        cout << "OVO JE ZMIJA" << endl;
                            int temp = dp[I][J];
                            dp[I][J] = min(dp[i][j], dp[I][J]);
                            if(temp > dp[I][J]) {
                                i = I;
                                j = J;
                            }
                        } else { // ladder
                        cout << "OVO JE LJESTVA" << endl;
                            dp[I][J] = min(dp[I][J], dp[i][j]);
                        }
                    }
                    prev_six.push(prev_six.top()+1);
                    prev_six.pop();
                    cout << "DP TABLE: " << endl;
                    for(int i = 0; i < n; i++) {
                        for(int j = 0; j < n; j++) {
                            cout << dp[i][j] << " ";
                        }
                        cout << endl;
                    }
                    cout << "DONE WITH DP TABLE" << endl;
                }
            }
        }
        if(n % 2 == 0)
            return dp[0][0];
        else return dp[0][n-1];
    }
};
int main() {
    Solution sol;
    vector<vector<int>> board{
        {-1,-1,-1,-1,-1,-1},
        {-1,-1,-1,-1,-1,-1},
        {-1,-1,-1,-1,-1,-1},
        {-1,35,-1,-1,13,-1},
        {-1,-1,-1,-1,-1,-1},
        {-1,15,-1,-1,-1,-1}
        };
    cout << sol.snakesAndLadders(board);
}