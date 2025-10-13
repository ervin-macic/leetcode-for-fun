class Solution {
public:
    string addBinary(string a, string b) {
        int idxA = a.size() - 1;
        int idxB = b.size() - 1;
        int carry = 0;
        string ans = "";
        while(idxA >= 0 && idxB >= 0) {
            if(a[idxA] == '1' && b[idxB] == '1') {
                if(carry) {
                    ans.push_back('1');
                } else {
                    ans.push_back('0');
                    carry = 1;
                }
            } else if((a[idxA] == '1' && b[idxB] == '0') || (a[idxA] == '0' && b[idxB] == '1')) {
                if(carry) {
                    ans.push_back('0');
                } else {
                    ans.push_back('1');
                }
            } else {
                if(carry) {
                    ans.push_back('1');
                    carry = 0; 
                } else {
                    ans.push_back('0');
                }
            }
            idxA--;
            idxB--;
        }
        while(idxA >= 0) {
            if(a[idxA] == '1' && carry) {
                ans.push_back('0');
            } else if(a[idxA] == '0' && carry) {
                ans.push_back('1');
                carry = 0;
            } else {
                ans.push_back(a[idxA]);
            }
            idxA--;
        }
        while(idxB >= 0) {
            if(b[idxB] == '1' && carry) {
                ans.push_back('0');
            } else if(b[idxB] == '0' && carry) {
                ans.push_back('1');
                carry = 0;
            } else {
                ans.push_back(b[idxB]);
            }
            idxB--;
        }
        if(carry) ans.push_back('1');
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
