#include <bits/stdc++.h>

using namespace std;
    void dfs(const vector<vector<int>> &graph, unordered_map<int, bool> &visited, int source) {
        cout << source << endl;
        visited[source] = true;
        for(auto neighbor : graph[source]) {
            if(visited[neighbor] == false) {
                dfs(graph, visited, neighbor);
            }
        }
    }
    void bfs(const vector<vector<int>> &graph, unordered_map<int, bool> &visited, vector<int> &distances, int source) {
        queue<int> q;
        q.push(source);
        distances[source] = 0;
        visited[source] = true;
        while(!q.empty()) {
            int u = q.front();
            cout << u << endl;
            q.pop();
            for(auto neighbor : graph[u]) {
                if(!visited[neighbor]) {
                    visited[neighbor] = true;
                    distances[neighbor] = distances[u] + 1;
                    q.push(neighbor);
                }
            }
        }
    }
int mainGraphs()
{
    int V;
    cout << "Number of vertices in graph: ";
    cin >> V;
    vector<vector<int>> graph(V);
    unordered_map<int, bool> visited;
    int E;
    cout << "Number of edges in graph: ";
    cin >> E;
    for(int i = 0; i < E; i++) {
        cout << "Input " << i << "th edge: ";
        int u,v;
        cin >>  u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    // DFS
    for(int v = 0; v < V; v++) {
        if(visited[v] == false) {
            dfs(graph, visited, v);
        }
    }
    visited.clear();
    cout << "Now BFS: \n";
    // BFS
    vector<int> distances(V, -1);
    bfs(graph, visited, distances, 0);
    for(int i = 0; i < V; i++) {
        cout << i << ": " << distances[i] << endl;
    }
}
int main() {

}
