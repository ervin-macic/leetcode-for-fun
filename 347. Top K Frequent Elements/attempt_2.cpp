#include<iostream>
#include<vector>
#include<queue>
#include<unordered_map>

using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        for(int x : nums)
            freq[x]++;
        priority_queue<
            pair<int,int>,
            vector<pair<int,int>>,
            greater<pair<int,int>>
        > pq;

        for(auto& [num, f] : freq) {
            pq.push({f, num});
            if(pq.size() > k)
                pq.pop();
        }

        vector<int> result;
        while(!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};
int main() {
    Solution sol;
    vector<int> nums = {1,2,1,2,1,2,3,1,3,2};
    for(auto x : sol.topKFrequent(nums, k)) {
        cout << x << " ";
    }
}