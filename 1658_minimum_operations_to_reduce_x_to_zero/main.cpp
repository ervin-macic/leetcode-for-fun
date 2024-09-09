#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int len = nums.size();
        int glob_max = 0;

        int left = 0;
        int right = 0;

        long long cur_sum = nums[0];
        if(cur_sum == x) return 1;
        long long arr_sum = 0;
        for(int i = 0; i < len; i++){
            arr_sum += nums[i];
        }
        //cout << "Arr sum: " << arr_sum << endl;
        if(arr_sum == x) return len;
        int target = arr_sum - x;
        while(left <= right + 1 and right <= len - 1){
            //cout << left << " " << right << " " << cur_sum << endl;
            if(cur_sum < target){
                    //cout << "I'm here 1" << endl;
                right++;
                cur_sum += nums[right];
            }else if(cur_sum > target){
                //cout << "I'm here 2" << endl;
                cur_sum -= nums[left];
                left++;
            }else{
                //cout << "I'm here 3" << endl;
                if((right - left + 1) > glob_max){
                    glob_max = right - left + 1;

                }
                cur_sum -= nums[left];
                left++;

                if(left == right + 1){
                    right++;
                    cur_sum += nums[right];
                }
                //cout << left << " " << right << " " << cur_sum << endl;
            }
        }
        int ans = len - glob_max;
        return (glob_max != 0)? ans : -1;
    }
};
int main()
{
    vector<int> nums = {1,1,4,2,3};
    int x = 5;
    Solution solution;

    cout << solution.minOperations(nums, x) << endl;

}
