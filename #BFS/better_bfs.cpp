#include<bits/stdc++.h>
using namespace std;
void BFS(int n, vector<vector<int>> graph, int source) {
    queue<int> q;
    unordered_map<int, bool> visited;
    q.push(source);
    while(!q.empty()) {
        int curr = q.front();
        cout << curr << endl;
        visited[curr] = true;
        q.pop();
        for(auto neighbor : graph[curr]) {
            if(!visited[neighbor]) {
                q.push(neighbor);
            }
        }
    }
}
int main() {
    int n = 6;
    vector<vector<int>> graph(n+1);
    graph[1] = {2,4};
    graph[2] = {1,3,5};
    graph[3] = {2,6};
    graph[4] = {1};
    graph[5] = {2,6};
    graph[6] = {3,5};
    int source = 1;
    BFS(n, graph, source);
}