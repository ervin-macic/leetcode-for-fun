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
    long long ans;
    int maxPathSum(TreeNode* root) {
        ans = root->val;
        maxSumHelper(root)
        return ans;
    }
    int maxSumHelper(TreeNode* root) {
        if(root == nullptr) return 0;
        int leftPathSum = max(0, maxSumHelper(root->left));
        int rightPathSum = max(0, maxSumHelper(root->right, res));
        ans = max(ans, leftPathSum + rightPathSum + root->val);
        return max(leftPathSum, rightPathSum) + root->val; // so return the maximum path rooted at this root
    }
};