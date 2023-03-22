#include <bits/stdc++.h>

using namespace std;
vector<vector<int>> graph;
unordered_map<int, bool> visited;
queue<int> q;
bool actual_source = false;
void BFS(int source){
    cout << source << endl;
    visited[source] = true;
    if(actual_source == false) q.push(source);
    actual_source = true;
    for(int i = 0; i < graph[source].size(); i++){
        if(visited[graph[source][i]] == false){
            q.push(graph[source][i]);
        }
    }
    q.pop();
    if(!q.empty()){
        BFS(q.front());
    }
}
int main()
{
    int edges, nodes;
    cout << "Input number of nodes: " << endl;
    cin >> nodes;
    cout << "Input number of edges: " << endl;
    cin >> edges;
    graph.resize(nodes);
    for(int i = 0; i < edges; i++){
        int edge_1, edge_2;
        cin >> edge_1;
        cin >> edge_2;
        graph[edge_1].push_back(edge_2);
        graph[edge_2].push_back(edge_1);
    }
    int source;
    cout << "Give me the source: " << endl;
    cin >> source;
    // run the algorithm:
    BFS(source);
}
