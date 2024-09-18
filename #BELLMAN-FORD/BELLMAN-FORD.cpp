#include<bits/stdc++.h>
using namespace std;
vector<int> bellmanFord(int n, vector<tuple<int, int, int>> edge_list, int source) {
    vector<int> distance(n+1, INT_MAX);
    distance[source] = 0;
    for(int i = 0; i < n-1; i++) {
        for(auto edge : edge_list) {
            int a,b,w;
            tie(a,b,w) = edge;
            if(distance[a] < INT_MAX) {
                distance[b] = min(distance[b], distance[a]+w);
            }
        }
    }
    return distance;
}
int main() {
    vector<tuple<int, int, int>> edges{
        {1,2,5},
        {1,3,3},
        {1,4,7},
        {2,4,3},
        {2,5,2},
        {3,4,1},
        {4,5,2},
        {2,1,5},
        {3,1,3},
        {4,1,7},
        {4,2,3},
        {5,2,2},
        {4,3,1},
        {5,4,2}
    };
    int n = 5;
    vector<int> dist = bellmanFord(n, edges, 1);
    int idx = 1;
    for(int i = 1; i <= n; i++){
        cout << i << ": " << dist[i] << endl;
    }

    return 0;
}