#include<bits/stdc++.h>
using namespace std;
bool isBipartite(int n, vector<vector<int>> graph, unordered_map<int, bool>& visited, unordered_map<int, char>& color, int curr=1) {
    visited[curr] = true;
    for(auto neighbor : graph[curr]) {
        if(visited[neighbor] and color[neighbor] == color[curr]) {
            return false;
        }
        if(!visited[neighbor]) {
            color[neighbor] = (color[curr] == 'B') ? 'R' : 'B';
            if(!isBipartite(n, graph, visited, color, neighbor)) return false;
        }
    }
    return true;
}
int main() {
    int n = 5;
    vector<vector<int>> not_bipartite_graph(n+1);
    not_bipartite_graph[1] = {2,4};
    not_bipartite_graph[2] = {1,3,5};
    not_bipartite_graph[3] = {2,5};
    not_bipartite_graph[4] = {1,5};
    not_bipartite_graph[5] = {2,3,4};

    vector<vector<int>> bipartite_graph(n+1);
    bipartite_graph[1] = {2};
    bipartite_graph[2] = {1,5};
    bipartite_graph[3] = {5};
    bipartite_graph[4] = {5};
    bipartite_graph[5] = {2,3,4};

    unordered_map<int, bool> visited;
    unordered_map<int, char> color;
    color[1] = 'B';
    cout << isBipartite(n, bipartite_graph, visited, color);
}