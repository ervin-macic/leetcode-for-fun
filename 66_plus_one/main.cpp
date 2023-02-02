#include <bits/stdc++.h>

using namespace std;
//class Solution {
//public:
//    vector<int> plusOne(vector<int>& digits) {
//        int current = digits.size() - 1;
//        vector<int> answer;
//        int numOf9 = 0;
//        while(current >= 0){
//            if(digits[current] == 9){
//                numOf9++;
//            }else{
//            break;
//            }
//            current--;
//        }
//        cout << numOf9 << endl;
////        if(numOf9 == 0){
////            answer.push_back(digits[digits.size() - 1] + 1);
////            for(int i = digits.size() - 2; i >= 0; i--){
////                answer.push_back(digits[i]);
////            }
////            reverse(answer.begin(), answer.end());
////        }else{
//            if(numOf9 != digits.size()){
//                for(int i = digits.size() - 1;  i >= digits.size() - numOf9; i--){
//                    answer.push_back(0);
//                }
//                answer.push_back(digits[digits.size() - numOf9 - 1] + 1);
//                for(int i = digits.size() - numOf9 - 2; i >= 0; i--){
//                    answer.push_back(digits[i]);
//                }
//                reverse(answer.begin(), answer.end());
//            }else{
//            answer.push_back(1);
//            for(int i = 0; i < digits.size(); i++) answer.push_back(0);
//            }
//        //}
//
//        return answer;
//    }
//};
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int cnt = digits.size() - 1;
        while(cnt >= 0){
            if(digits[cnt] != 9){
                digits[cnt]++;
                return digits;
            }else{
                digits[cnt] = 0;
            }
            cnt--;
        }
        digits[0] = 1;
        digits.push_back(0);
        return digits;
    }
};
int main()
{
    vector<int> digits{1,2,3,3,9,9,9,9};
    Solution sol;
    vector<int> newVec = sol.plusOne(digits);
    for(auto x : newVec) cout << x << " ";
}
