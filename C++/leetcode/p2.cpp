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
//单纯遍历了一遍链表
class Solution {
public:
    int qwe(int &cin,int l1,int l2){
        int n=cin+l1+l2;
        cin=n/10;
        return n%10;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int cin=0;
        int x1=0,x2=0;
        ListNode* t1=l1;ListNode* t2=l2;
        while (t1) {
            x1++;
            t1=t1->next;
        }
        while (t2) {
            x2++;
            t2=t2->next;
        }
        if(x1<x2){
            t1=l1;
            l1=l2;
            l2=t1;
        }
        ListNode* ans=new ListNode(qwe(cin , l1->val , l2->val));
        l1=l1->next;l2=l2->next;
        ListNode* ant=ans;
        while(l2){
            ant->next=new ListNode(qwe(cin , l1->val , l2->val));
            ant=ant->next;l1=l1->next;l2=l2->next;
        }
        while(l1){
            ant->next=new ListNode(qwe(cin , l1->val , 0));
            ant=ant->next;l1=l1->next;
        }
        if(cin!=0)ant->next=new ListNode(cin);
        return ans;
    }
};