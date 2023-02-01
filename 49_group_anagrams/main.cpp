#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

        vector<string> copyCat = strs;
        vector<vector<string>> answer;

        int uniquePosition = 0;
        unordered_map<string, int> seenWhere; // "ant" to its position in the answer string aet 0 ant 1 abt 2
        int len = copyCat.size();
        answer.resize(len);
        for(int i = 0; i < len; i++){
            sort(copyCat[i].begin(), copyCat[i].end());
            if(seenWhere.count(copyCat[i]) == 0){
                seenWhere[copyCat[i]] = uniquePosition;
                uniquePosition++;
            }
            answer[seenWhere[copyCat[i]]].push_back(strs[i]);
        }
        // cleaning of empty slots:
        for(int i = (int)answer.size() - 1; i >= 0; i--){
            if(answer[i].empty()){
                answer.pop_back();
            }else{
                break;
            }
        }
        return answer;
    }
};
int main()
{
    vector<string> strs{"eat", "tea", "tan", "ate", "nat", "bat"};
    Solution sol;
    vector<vector<string>> ans = sol.groupAnagrams(strs);
    for(int i = 0; i < (int)ans.size(); i++){
        for(int j = 0; j < (int)ans[i].size(); j++){
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}
