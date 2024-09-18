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
    unordered_map<int, int> distance;
    unordered_map<int, bool> visited;
    int BFS(auto graph, int source, int target) {
        queue<int> q;
        visited[source] = true;
        distance[source] = 0;
        q.push(source);
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            for(int i = 0; i < graph[curr].size(); i++) {
                int next = graph[curr][i];
                if (!visited[next]) {
                    visited[next] = true;
                    distance[next] = distance[curr] + 1;
                    q.push(next);
                } else if (distance[next] > distance[curr] + 1) {
                    distance[next] = distance[curr] + 1;
                    q.push(next);
                }
            }
        }
        return distance[target];
    }
    int snakesAndLadders(vector<vector<int>>& board) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        int n = board.size();
        vector<vector<int>> graph;
        graph.resize(n*n+1);
        int I,J;
        for(int idx = 1; idx <= n*n; idx++) {
            for(int j = 1; j <= 6 and (idx+j) <= n*n; j++) {
                graph[idx].push_back(idx+j);
            }
            pair<int, int> indices = get_i_j(n, idx);
            I = indices.first;
            J = indices.second;
            if(board[I][J] != -1 and find(graph[idx].begin(), graph[idx].end(), board[I][J]) == graph[idx].end()) {
                graph[idx].push_back(board[I][J]);
            }
        }
        for(int idx = 1; idx <= n*n; idx++) {
            cout << idx << ": ";
            for(int j = 0; j < graph[idx].size(); j++) {
                cout << graph[idx][j] << " ";
            }
            cout << endl;
        }

        int distance = BFS(graph, 1, n*n);
        return distance;
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
       /*  vector<vector<int>> board{
            {-1,-1},
            {-1,3}
        }; */
    cout << sol.snakesAndLadders(board);
}