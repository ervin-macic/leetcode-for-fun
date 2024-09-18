#include<bits/stdc++.h>
using namespace std;

bool isBipartiteComponent(int node, vector<vector<int>>& graph, unordered_map<int, bool>& visited, unordered_map<int, char>& color) {
    visited[node] = true;
    for(auto neighbor : graph[node]) {
        if(visited[neighbor] && color[neighbor] == color[node]) {
            return false; // Conflict in coloring
        }
        if(!visited[neighbor]) {
            color[neighbor] = (color[node] == 'B') ? 'R' : 'B';
            if(!isBipartiteComponent(neighbor, graph, visited, color)) 
                return false;
        }
    }
    return true;
}

bool isBipartite(int n, vector<vector<int>>& graph) {
    unordered_map<int, bool> visited;
    unordered_map<int, char> color;
    
    for(int i = 1; i <= n; i++) {
        if(!visited[i]) {
            color[i] = 'B'; // Start coloring with 'B' for unvisited components
            if(!isBipartiteComponent(i, graph, visited, color))
                return false;
        }
    }
    return true;
}

int main() {
    int n = 5;
    
    // Not bipartite graph
    vector<vector<int>> not_bipartite_graph(n+1);
    not_bipartite_graph[1] = {2,4};
    not_bipartite_graph[2] = {1,3,5};
    not_bipartite_graph[3] = {2,5};
    not_bipartite_graph[4] = {1,5};
    not_bipartite_graph[5] = {2,3,4};

    // Bipartite graph
    vector<vector<int>> bipartite_graph(n+1);
    bipartite_graph[1] = {2};
    bipartite_graph[2] = {1,5};
    bipartite_graph[3] = {5};
    bipartite_graph[4] = {5};
    bipartite_graph[5] = {2,3,4};

    cout << "Bipartite Graph: " << isBipartite(n, bipartite_graph) << endl;  // Expected output: 1 (true)
    cout << "Not Bipartite Graph: " << isBipartite(n, not_bipartite_graph) << endl;  // Expected output: 0 (false)

    return 0;
}
