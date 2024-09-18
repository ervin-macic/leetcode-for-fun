#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    unordered_map<string, vector<string>> adj;
    unordered_map<string, bool> visited;
    int neighbors(string s1, string s2) {
        if(s1.size() != s2.size()) return false;
        int diff = 0;
        for(int i = 0; i < s1.size(); i++) {
            if(s1[i] != s2[i]) {
                diff++;
            }
            if(diff > 1) return -1;
        }
        return diff;
    }
    
    int BFS(string source, string target){
        queue<string> q;
        unordered_map<string, int> dist;
        visited[source] = true;
        q.push(source);
        dist[source] = 0;
        while(!q.empty()) {
            string curr = q.front();
            q.pop();
            for(int i = 0; i < adj[curr].size(); i++){
                if(visited[adj[curr][i]] == false){
                    visited[adj[curr][i]] = true;
                    dist[adj[curr][i]] = dist[curr] + 1;
                    q.push(adj[curr][i]);
                    // cout << "RIJEC: " << adj[curr][i] << " je udaljena: " << dist[adj[curr][i]] << endl;
                }
                if(adj[curr][i] == target) {
                    return dist[adj[curr][i]];
                }
            }
        }
        return -1;
    }
    bool in_list(string word, vector<string> list) {
        for(auto w : list) {
            if(word == w) return true;
        }
        return false;
    }
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        if(!in_list(endWord, wordList)) return 0;
        if(neighbors(beginWord, endWord) == 0) return 1;
        if(neighbors(beginWord, endWord) == 1) return 2;
        int n = wordList.size();
        for(int i = 0; i < n; i++) {
            if(neighbors(beginWord, wordList[i]) == 1) {
                adj[beginWord].push_back(wordList[i]);
                adj[wordList[i]].push_back(beginWord);
            }
            if(neighbors(endWord, wordList[i]) == 1) {
                adj[endWord].push_back(wordList[i]);
                adj[wordList[i]].push_back(endWord);
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                if(neighbors(wordList[i], wordList[j]) == 1){
                    adj[wordList[i]].push_back(wordList[j]);
                    adj[wordList[j]].push_back(wordList[i]);
                }
            }
        }
        int distance = BFS(beginWord, endWord);
        return distance+1;
    }
};

int main() {
    Solution sol;
    string a = "hot";
    string b = "dog";
    vector<string> wordList = {"hot","dog","cog","pot","dot"}; // expected hot dot dog (dog ima distance 2)
    cout << sol.ladderLength(a, b, wordList);
}