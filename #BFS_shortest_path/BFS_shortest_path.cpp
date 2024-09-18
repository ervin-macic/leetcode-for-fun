#include<bits/stdc++.h>
using namespace std;
vector<int> BFS_shortest_path(int n, vector<vector<int>> graph, int source) {
    queue<int> q;
    unordered_map<int, bool> visited;
    vector<int> distance(n+1, INT_MAX);
    distance[source] = 0;
    q.push(source);
    while(!q.empty()) {
        int curr = q.front();
        visited[curr] = true;
        q.pop();
        for(auto neighbor : graph[curr]) {
            if(!visited[neighbor]) {
                distance[neighbor] = distance[curr] + 1;
                q.push(neighbor);
            }
        }
    }
    return distance;
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
    vector<int> distance = BFS_shortest_path(n, graph, source);
    cout << "node distance" << endl;
    cout << "-------------" << endl;
    for(int i = 1; i <= n; i++) {
        cout << i << "    " << distance[i] << endl;
    }
}