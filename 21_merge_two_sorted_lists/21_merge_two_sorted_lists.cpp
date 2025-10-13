#include<bits/stdc++.h>
using namespace std;
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class ListNode {
public:
    int val;
    ListNode* next;

    // Constructor
    ListNode(int value, ListNode* nextNode = nullptr)
        : val(value), next(nextNode) {}
};
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
        ListNode* result = new ListNode(0);
        ListNode* ans = result;
        while(a != nullptr && b != nullptr) {
            if(a->val > b->val) {
                result->next = b;
                b = b->next;
            } else {
                result->next = a;
                a = a->next;
            }
            result = result->next;
        }
        if(a != nullptr) result->next = a;
        if(b != nullptr) result->next = b;
        return ans->next;
    }
};
int main() {
    Solution sol = Solution();
    auto a = &ListNode(1, ListNode(2, ListNode(4, nullptr)));
    auto b = &ListNode(1, ListNode(3, ListNode(4, nullptr)));
    auto ans = sol.mergeTwoLists(a,b);
    auto ptr = ans;
    while(ptr) {
        cout << ptr.val << " ";
        ptr = ptr->next;
    }
}