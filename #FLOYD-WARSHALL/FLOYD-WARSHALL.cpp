#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> floydWarshall(int n, vector<vector<pair<int, int>>> graph) {
    vector<vector<int>> distance (n+1, vector<int>(n+1, INT_MAX));
    for(int a = 1; a <= n; a++) {
        distance[a][a] = 0;
    }
    for(int a = 1; a <= n; a++) {
        for(auto u : graph[a]) {
            int b = u.first;
            int w = u.second;
            distance[a][b] = w;
        }
    }
    for(int a = 1; a <= n; a++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                if(distance[i][a] < INT_MAX && distance[a][j] < INT_MAX) {
                    distance[i][j] = min(distance[i][j], distance[a][j] + distance[i][a]);
                }
            }
        }
    }
    return distance;
}
int main() {
    int n = 5;
    vector<vector<pair<int, int>>> graph(n + 1); 

    graph[1] = {{2, 5}, {5, 1}, {4, 9}};
    graph[2] = {{1, 5}, {3, 2}};
    graph[3] = {{2, 2}, {4, 6}};
    graph[4] = {{1, 9}, {3, 6}, {5, 2}};
    graph[5] = {{1, 1}, {4, 2}};
    vector<vector<int>> distance = floydWarshall(n, graph);
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            cout << distance[i][j] << " ";
        }
        cout << endl;
    }
}