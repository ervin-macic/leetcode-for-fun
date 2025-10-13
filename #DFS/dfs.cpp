#include <bits/stdc++.h>
using namespace std;

void DFS(const vector<vector<int>> &graph, unordered_map<int, bool> &visited, int source){
    cout << source << endl;
    visited[source] = true;
    for(auto neighbor : graph[source])
        if(!visited[neighbor]) 
            DFS(graph, visited, neighbor);
}
int main()
{
    int V, E;
    cout << "Input number of vertices: " << endl;
    cin >> V;
    cout << "Input number of edges: " << endl;
    cin >> E;
    vector<vector<int>> graph(V);
    unordered_map<int, bool> visited;
    for(int i = 0; i < E; i++){
        int u, v;
        cout << "Input the " << i+1 << ". edge (two vertices):\n";
        cin >> u;
        cin >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    int source;
    cout << "Start DFS from node: ";
    cin >> source;
    DFS(graph, visited, source);
}
