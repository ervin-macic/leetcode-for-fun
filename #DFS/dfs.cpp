#include <bits/stdc++.h>
using namespace std;

template<typename Map>
    void DFS(auto graph, Map visited, int vertex){
        cout << vertex << endl;
        visited[vertex] = true;
        for(auto neighbor : graph[vertex])
            if(!visited[neighbor]) 
                DFS(graph, visited, neighbor);
    }
int main()
{
    int edges, nodes;
    cout << "Input number of nodes: " << endl;
    cin >> nodes;
    cout << "Input number of edges: " << endl;
    cin >> edges;
    vector<vector<int>> graph(nodes);
    unordered_map<int, bool> visited;
    for(int i = 0; i < edges; i++){
        int v1, v2;
        cout << "Input the " << i+1 << ". edge (two vertices):\n";
        cin >> v1;
        cin >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }
    int source;
    cout << "Where are we starting the depth-first-search? Give me the source node: " << endl;
    cin >> source;
    // run the algorithm:
    DFS(graph, visited, source);
}
