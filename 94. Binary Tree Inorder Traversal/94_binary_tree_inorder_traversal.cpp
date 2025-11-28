/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    vector<int> inorderTraversal(TreeNode* root) {
        if(root->left == nullptr && root->right == nullptr) return {root->val};
        if(root->left == nullptr) return inorderTraversal(root->right)
        vector<int> leftAns = inorderTraversal(root->left)
        leftAns.push_back(root->val);
        vector<int> rightAns = inorderTraversal(root->right);
        return ans.insert(ans.end(), rightAns.begin(), rightAns.end());
    }
};
int main() {
    // [1,2,3,4,5,null,8,null,null,6,7,9]
}