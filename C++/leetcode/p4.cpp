class Solution {
private:
    int qwe(vector<int>& nums1, vector<int>& nums2,int t1,int t2,int k){
        if(t1>=nums1.size()) return nums2[t2+k-1];
        if(t2>=nums2.size()) return nums1[t1+k-1];
        if(k==1) return min(nums1[t1], nums2[t2]);

        int n1=nums1.size();
        int n2=nums2.size();
        int x1=min(t1 + k / 2, (int)nums1.size());
        int x2=min(t2 + k / 2, (int)nums2.size());
        if(nums1[x1 - 1] < nums2[x2 - 1]) 
            return qwe(nums1,nums2,x1,t2,k+t1-x1);
        else
            return qwe(nums1,nums2,t1,x2,k+t2-x2);
    }

public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size();
        int n2=nums2.size();
        if((n1+n2)%2)
            return qwe(nums1,nums2,0,0,(n1+n2)/2+1);
        else
            return double(qwe(nums1,nums2,0,0,(n1+n2)/2)+qwe(nums1,nums2,0,0,(n1+n2)/2+1))/2;
    }
};