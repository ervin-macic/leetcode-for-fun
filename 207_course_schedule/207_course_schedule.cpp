#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool detect_cycle(const vector<vector<int>> &graph, vector<int> &state, int source) {
        state[source] = 1; 
        for (int neighbor : graph[source]) {
            if (state[neighbor] == 1) {
                return true;
            }
            if (state[neighbor] == 0 && detect_cycle(graph, state, neighbor)) {
                return true;
            }
        }
        state[source] = 2;
        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for (auto &edge : prerequisites) {
            graph[edge[1]].push_back(edge[0]);
        }

        vector<int> state(numCourses, 0);
        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0) {
                if (detect_cycle(graph, state, i)) {
                    return false; 
                }
            }
        }
        return true;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> prereqs = {{0,1}};
    cout << (sol.canFinish(2, prereqs) ? "true" : "false");
}
