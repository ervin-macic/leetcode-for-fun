#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int subarraySum(vector<int>& arr, int k) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        int n = arr.size();
        int cum_sum[n];
        cum_sum[0] = arr[0];
        for(int i = 1; i < n; i++){
            cum_sum[i] = arr[i] + cum_sum[i - 1];
        }
        unordered_map<int,int> hash; 
        int ans = 0;
        for(int i = 0; i < n; i++){
            if(cum_sum[i] == k) ans++;
            if(hash.find(cum_sum[i] - k) != hash.end()){
                ans += hash[cum_sum[i] - k];
            }
            hash[cum_sum[i]]++;
        }
        return ans;
    }
};
int main(){
    Solution sol;
    vector<int>nums = {1,-1,0}; //{3,2,1,4,3,3,1,2,5,2};
    cout << "ANS: " << sol.subarraySum(nums, 0);
}