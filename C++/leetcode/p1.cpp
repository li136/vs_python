
// 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
// 使用hash思想，快速检索对应数值是否存在
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mp;
        vector<int> ans;
        for(int i=0;i<nums.size();i++)
            mp[nums[i]]=i;
        for(int i=0;i<nums.size();i++){
        if(mp.find(target - nums[i]) != mp.end() && i != mp[target - nums[i]]){
            ans.push_back(i);
            ans.push_back(mp[target - nums[i]]);
            return ans;
        }
    }
    return ans;
    }
};