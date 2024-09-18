#include<bits/stdc++.h>
using namespace std;
vector<int> dijkstra(int n, vector<vector<pair<int, int>>> graph, int source) {
    vector<int> distance(n+1, INT_MAX);
    unordered_map<int, bool> processed;
    distance[source] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, source});
    while(!pq.empty()) {
        int a = pq.top().second;
        pq.pop();
        if(processed[a]) continue;
        processed[a] = true;
        for(auto u : graph[a]) {
            int b = u.first;
            int w = u.second;
            if(distance[b] > distance[a] + w) {
                distance[b] = distance[a] + w;
                pq.push({distance[b], b});
            }
        }
    }
    return distance;
}
int main()
{
    int n = 5;
    vector<vector<pair<int, int>>> graph{
        {},                          // (dummy node, as node indexing starts from 1)
        {{2, 5}, {5, 1}, {4, 9}},    
        {{1, 5}, {3, 2}},            
        {{2, 2}, {4, 6}},            
        {{1, 9}, {3, 6}, {5, 2}},
        {{1, 1}, {4, 2}}             
    };

    vector<int> dist = dijkstra(n, graph, 1);
    for(int i = 1; i <= n; i++) {
        cout << i << ": " << dist[i] << endl;
    }
    return 0;
}